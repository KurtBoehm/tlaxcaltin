# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Update Tlaxcaltin in a project that uses it, with steps that are detailed later
# in this file. Note that this requires “subprojects.txt” to exist in the root folder
# of the project using Tlaxcaltin.

import re
from collections import deque
from pathlib import Path
from shutil import move, rmtree
from subprocess import run
from tempfile import TemporaryDirectory
from typing import Final

_tlax_url: Final = "https://github.com/KurtBoehm/tlaxcaltin.git"
_folder_names: Final = {
    "boost-preprocessor": "preprocessor-boost",
    "combblas": "CombBLAS",
    "google-benchmark": "benchmark",
    "gtest": "googletest",
    "liblzma": "xz",
    "nlohmann-json": "nlohmann_json",
    "sdl2": "SDL2",
    "suitesparse": "SuiteSparse",
    "xmp-toolkit-sdk": "XMP-Toolkit-SDK",
}
_wrapdb_names: Final = {"fmt", "google-benchmark", "liblzma", "nlohmann-json"}
_dep_prefix: Final = "# dependencies: "


def _expand_selection(subprojects_path: Path, selection: set[str]) -> set[str]:
    queue = deque(selection)
    expanded = set(selection)
    while queue:
        current = queue.popleft()
        wrap_path = subprojects_path / f"{current}.wrap"
        if not wrap_path.exists():
            continue
        with open(wrap_path, "r") as f:
            txt = f.read()
        for line in txt.splitlines():
            if not line.startswith(_dep_prefix):
                continue
            for dep in line[len(_dep_prefix) :].split(","):
                dep = dep.strip()
                if dep not in expanded:
                    expanded.add(dep)
                    queue.append(dep)
    return expanded


def update(project_path: Path, add: bool):
    subprojects_path: Final = project_path / "subprojects"
    selection_path: Final = project_path / "subprojects.txt"

    selection: set[str] | None
    if not selection_path.exists():
        print("No subprojects file exists.")
        selection = None
    else:
        with open(selection_path, "r") as f:
            selection = {line.strip() for line in f.readlines()}

    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir).resolve()

        package_cache_path = subprojects_path / "packagecache"
        packagecache_tmp_path = tmp_path / "packagecache"

        has_packagecache = package_cache_path.exists()
        if has_packagecache:
            move(package_cache_path, packagecache_tmp_path)

        rmtree(subprojects_path)
        run(["git", "clone", _tlax_url, "subprojects"], check=True)
        rmtree(subprojects_path / ".git")
        rmtree(subprojects_path / "private")
        (subprojects_path / "pyproject.toml").unlink()

        # Remove all subprojects that are not desired
        if selection is not None:
            selection = _expand_selection(subprojects_path, selection)
            wrapdb_deps = _wrapdb_names & selection
            fnames = {_folder_names.get(entry, entry) for entry in selection}

            # Create read-me
            readme_path = subprojects_path / "ReadMe.md"
            with open(readme_path, "r") as f:
                readme = f.read()
            readme = readme[readme.find("## Licence\n") + 12 :]
            readme = readme.replace(
                "Tlaxcaltin",
                "[Tlaxcaltin](https://github.com/KurtBoehm/tlaxcaltin)",
            )
            readme = readme.splitlines()[: (4 if len(wrapdb_deps) > 0 else 1)]
            readme += [f"- `{wdb}`" for wdb in sorted(wrapdb_deps)]
            readme = "\n".join(readme) + "\n"
            with open(readme_path, "w") as f:
                f.write(readme)

            # Remove the WrapDB licence if none of those dependencies are used
            if len(wrapdb_deps) == 0:
                (subprojects_path / "LicenseWrapDB").unlink()

            # Remove wraps and direct subfolders
            for p in subprojects_path.iterdir():
                if p.is_file() and p.suffix == ".wrap":
                    if p.stem not in selection:
                        p.unlink()
                        continue
                if p.is_dir() and p.name not in fnames | {"packagefiles"}:
                    rmtree(p)

            # Remove package files
            package_files_path = subprojects_path / "packagefiles"
            for p in package_files_path.iterdir():
                if p.name not in selection | {"patch"}:
                    rmtree(p)
            if len(list(package_files_path.iterdir())) == 0:
                package_files_path.rmdir()

            # Remove patches
            patch_path = package_files_path / "patch"
            if patch_path.exists():
                for p in patch_path.iterdir():
                    if p.stem not in selection:
                        p.unlink()
                if len(list(patch_path.iterdir())) == 0:
                    patch_path.rmdir()

            # Clean up gitignore
            gitignore_path = subprojects_path / ".gitignore"
            with open(gitignore_path, "r") as f:
                gitignore = f.readlines()
            new_gitignore = []
            folder_re = re.compile(r"/(.*)-\*/")
            for line in gitignore:
                line = line.strip()
                if (m := folder_re.fullmatch(line)) is not None:
                    if m.group(1) in fnames:
                        new_gitignore.append(line)
                elif line not in ["__pycache__/"]:
                    new_gitignore.append(line)
            if new_gitignore[-1] == "":
                new_gitignore.pop()
            with open(gitignore_path, "w") as f:
                f.write("".join(f"{line!s}\n" for line in new_gitignore))

        if add:
            run(["git", "add", "subprojects"], check=True)

        if has_packagecache:
            move(packagecache_tmp_path, package_cache_path)
