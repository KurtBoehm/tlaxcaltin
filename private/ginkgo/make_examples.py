from pathlib import Path


for folder in Path().iterdir():
    if not folder.is_dir():
        continue
    build = (
        f"executable(\n"
        f"  '{folder.name}',\n"
        f"  '{folder.name}.cpp',\n"
        f"  dependencies: examples_deps,\n"
        f")"
    )
    data_folder = folder / "data"
    if data_folder.exists():
        build += "\nsubdir('data')"
        data_files = [p for p in data_folder.iterdir() if p.name != "meson.build"]
        with open(data_folder / "meson.build", "w") as f:
            print(
                "\n".join(
                    f"configure_file(copy: true, input: '{p.name}', output: '{p.name}')"
                    for p in data_files
                ),
                file=f,
            )
    with open(folder / "meson.build", "w") as f:
        print(build, file=f)
