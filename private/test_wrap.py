# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
from shutil import copy, copytree, rmtree, unpack_archive
from subprocess import run

from pydantic import BaseModel, Field, TypeAdapter
from requests import get


class Args(BaseModel):
    wrap: str


class WrapSection(BaseModel):
    directory: str | None = None
    patch_directory: str
    diff_files: str | None = None


class WrapFileSection(WrapSection):
    source_url: str
    source_filename: str
    source_hash: str


class WrapGitSection(WrapSection):
    url: str
    revision: str
    clone_recursive: bool = Field(alias="clone-recursive")


class FileWrap(BaseModel):
    wrap_body: WrapFileSection = Field(alias="wrap-file")
    provide: dict[str, str]


class GitWrap(BaseModel):
    wrap_body: WrapGitSection = Field(alias="wrap-git")
    provide: dict[str, str]


Wrap = FileWrap | GitWrap


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

wrap = TypeAdapter(Wrap).validate_python(d)
assert isinstance(wrap, Wrap)
body = wrap.wrap_body
directory = body.directory if body.directory else wrap_path.stem

pkg_base_folder = base_path / "packagecache"
pkg_base_folder.mkdir(exist_ok=True)
pkg_folder = pkg_base_folder / directory
print(pkg_folder)

match body:
    case WrapFileSection():
        cmp_path = pkg_base_folder / body.source_filename
        if not cmp_path.exists():
            data = get(body.source_url).content
            with open(cmp_path, "wb") as f:
                f.write(data)

        unpack_archive(cmp_path, pkg_base_folder)
    case WrapGitSection():
        if pkg_folder.exists():
            rmtree(pkg_folder)
        clone_cmd = [
            "git",
            "clone",
            *(["--recurse-submodules"] if body.clone_recursive else []),
            body.url,
            pkg_folder,
        ]
        run(clone_cmd)

        if body.revision.lower() != "head":
            run(["git", "checkout", body.revision], cwd=pkg_folder)

# Apply patch directory
patch_base_path = base_path / "packagefiles" / body.patch_directory
for p in patch_base_path.iterdir():
    outp = pkg_folder / p.name
    print(f"Copy {p} to {outp}")
    if p.is_dir():
        copytree(p, outp, dirs_exist_ok=True)
    else:
        copy(p, outp)

# Apply diff files (patches)
if body.diff_files and (diff_files_str := body.diff_files.strip()):
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
