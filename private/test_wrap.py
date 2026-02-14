# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
from shutil import copy, copytree, unpack_archive

from pydantic import BaseModel, Field
from requests import get


class Args(BaseModel):
    wrap: str


class WrapFileSection(BaseModel):
    directory: str
    source_url: str
    source_filename: str
    source_hash: str
    patch_directory: str
    diff_files: str | None = None


class FileWrap(BaseModel):
    wrap_file: WrapFileSection = Field(alias="wrap-file")
    provide: dict[str, str]


parser = ArgumentParser(
    description="Test a wrap by downloading the source files, "
    + "unpacking them in the packagecache subfolder, "
    + "applying the patch directory, "
    + "applying the diff files, "
    + "and copying Tlaxcaltin into the subproject’s packagefiles."
)
parser.add_argument("wrap")
args = Args.model_validate(vars(parser.parse_args()))

base_path = Path(__file__).parents[1]
wrap_path = base_path / f"{args.wrap}.wrap"
with open(wrap_path, "r") as f:
    d = ConfigParser()
    d.read_file(f)
    d = {s: dict(d.items(s)) for s in d.sections()}

wrap = FileWrap.model_validate(d)

pkg_base_folder = base_path / "packagecache"
pkg_base_folder.mkdir(exist_ok=True)

cmp_path = pkg_base_folder / wrap.wrap_file.source_filename
if not cmp_path.exists():
    data = get(wrap.wrap_file.source_url).content
    with open(cmp_path, "wb") as f:
        f.write(data)

unpack_archive(cmp_path, pkg_base_folder)
pkg_folder = pkg_base_folder / wrap.wrap_file.directory
print(pkg_folder)

# Apply patch directory
patch_base_path = base_path / "packagefiles" / wrap.wrap_file.patch_directory
for p in patch_base_path.iterdir():
    outp = pkg_folder / p.name
    if p.is_dir():
        copytree(p, outp, dirs_exist_ok=True)
    else:
        copy(p, outp)

# Apply diff files (patches)
if wrap.wrap_file.diff_files and (diff_files_str := wrap.wrap_file.diff_files.strip()):
    diff_files = diff_files_str.split(",")
    for rel_diff in diff_files:
        diff_path = base_path / "packagefiles" / rel_diff
        if not diff_path.is_file():
            raise FileNotFoundError(f"Diff file not found: {diff_path}")
        # Apply with 'patch -p1' in the extracted source dir
        subprocess.run(
            ["patch", "-p1", "-i", str(diff_path)],
            cwd=pkg_folder,
            check=True,
        )

# Copy wrap files and auxiliary subprojects
subproj_path = pkg_folder / "subprojects"
subproj_path.mkdir(exist_ok=True)

for p in base_path.iterdir():
    outp = subproj_path / p.name
    if p.suffix == ".wrap":
        copy(p, outp)
    if p.is_dir() and p.name in ("blas_compat", "mpi-c", "mpi-cpp"):
        copytree(p, outp, dirs_exist_ok=True)

copytree(
    base_path / "packagefiles",
    subproj_path / "packagefiles",
    dirs_exist_ok=True,
)
