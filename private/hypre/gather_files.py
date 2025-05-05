# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Gather the files required by hypre and print them to simplify build file creation.

import re
from pathlib import Path

base = Path(__file__).parent
src = base / "src"

files_re = re.compile(
    r"\n(?:CU)?FILES *= *\\\n((?: *[^\\\n]+ *\\ *\n)+(?: *[^\\\n]+ *\n))"
)

folders = [f for f in src.iterdir() if f.is_dir()]
folders += [folder for f in folders for folder in f.iterdir() if folder.is_dir()]

for folder in sorted(folders, key=lambda p: str(p).lower()):
    make_path = folder / "Makefile"
    if not make_path.exists():
        continue
    # print(make_path)

    with open(make_path, "r") as f:
        make = f.read()
    ms = list(files_re.finditer(make))
    if len(ms) == 0:
        continue
    files = [
        str((folder / s.strip()).relative_to(base))
        for m in ms
        for s in m.group(1).split("\\\n")
    ]
    print("\n".join(sorted(files, key=lambda s: s.lower())))
