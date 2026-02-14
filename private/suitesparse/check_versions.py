# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from argparse import ArgumentParser
from pathlib import Path

major_re = re.compile(r"set \( .*_VERSION_MAJOR *(\d+)( CACHE STRING \"\" FORCE)? \)")
minor_re = re.compile(r"set \( .*_VERSION_MINOR *(\d+)( CACHE STRING \"\" FORCE)? \)")
sub_re = re.compile(r"set \( .*_VERSION_SUB *(\d*)( CACHE STRING \"\" FORCE)? \)")
meson_re = re.compile(r"version *: *'([^']*)'")

parser = ArgumentParser(
    description=(
        "Compare the versions of the SuiteSparse packages "
        "specified in the CMakeLists.txt files to those in the meson file "
        "and list those which differ."
    )
)
parser.add_argument("project", type=Path)
args = parser.parse_args()
project: Path = args.project

for folder in sorted(project.iterdir()):
    meson_path = folder / "meson.build"
    cmake_path = folder / "CMakeLists.txt"
    if not meson_path.exists() or not cmake_path.exists():
        continue

    cmake = cmake_path.read_text(encoding="utf-8")
    [major] = major_re.findall(cmake)
    [minor] = minor_re.findall(cmake)
    [sub] = sub_re.findall(cmake)
    major, minor, sub = major[0], minor[0], sub[0]
    version = f"{major}.{minor}.{sub}"

    meson = meson_path.read_text(encoding="utf-8")
    versions: list[str] = meson_re.findall(meson)
    wrong = [v for v in versions if v not in (version, major)]

    if len(wrong) > 0:
        print(f"{folder}: {wrong=} {version=}")
