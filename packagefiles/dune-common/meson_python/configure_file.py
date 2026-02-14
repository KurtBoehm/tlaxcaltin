# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from argparse import ArgumentParser
from pathlib import Path


def split_config(config_str: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in config_str.splitlines():
        index = line.index("=")
        out[line[:index]] = line[index + 1 :]
    return out


def index(
    sub: str,
    text: str,
    start: int | None = None,
) -> int | None:
    try:
        return text.index(sub, start)
    except ValueError:
        return None


def compute_private(contents: str) -> str:
    prefix = "\n/* begin private */\n"
    suffix = "\n/* end private */\n"

    pairs: list[tuple[int, int]] = []
    pres: list[int] = []

    i = 0
    while (isuf := index(suffix, contents, i)) is not None:
        ipre = index(prefix, contents, i)
        if ipre is not None and ipre < isuf:
            pres.append(ipre)
            i = ipre + len(prefix)
            continue
        ipre = pres.pop()
        isufend = isuf + len(suffix)
        pairs.append((ipre, isufend))
        i = isufend

    pairs += [(i, i + len(prefix)) for i in pres]
    pairs.sort()

    out = ""
    start = 0
    for ipre, isuf in pairs:
        out += f"{contents[start:ipre]}\n"
        start = isuf
    return out + contents[start:]


class Ns:
    def __init__(self):
        self.in_paths: list[Path]
        self.out_path: Path
        self.config: str


parser = ArgumentParser(description="Configure a file")
parser.add_argument(
    "in_paths",
    nargs="+",
    type=Path,
    help="The path of the file to configure",
)
parser.add_argument(
    "out_path",
    type=Path,
    help="The path of the file to configure",
)
parser.add_argument(
    "config",
    type=str,
    help="The parameters to configure the file with",
)
args = parser.parse_args(namespace=Ns())
join_paths = [p.resolve() for p in args.in_paths[:-1]]
in_path = args.in_paths[-1].resolve()
out_path = args.out_path.resolve()
config = split_config(args.config)

with open(out_path, "w") as out_file:
    for p in join_paths:
        with open(p, "r") as in_file:
            out_file.write(compute_private(in_file.read()) + "\n")

    with open(in_path, "r") as in_file:
        for line in in_file.readlines():
            prefix = "#cmakedefine"
            if line.startswith(prefix):
                key_start = line.index(" ") + 1
                key_end = index(" ", line, key_start)
                if key_end is None:
                    key_end = len(line) - 1
                    value_start = None
                else:
                    value_start = key_end + 1

                key = line[key_start:key_end]
                value = config.get(key, None)
                if value is None or value == "0":
                    line = f"/* #undef {key} */"
                else:
                    parts = ["#define", key]
                    if value_start is not None:
                        parts.append(line[value_start:-1])
                    line = " ".join(parts)

            i = 0
            while i < len(line):
                c = line[i]

                if c == "$":
                    assert line[i + 1] == "{"
                    start_index = i + 2
                    end_index = line.index("}", start_index)
                    value = config[line[start_index:end_index]]
                    line = line[:i] + value + line[end_index + 1 :]
                    i += len(value)
                    continue

                if c == "@":
                    start_index = i + 1
                    end_index = line.index("@", start_index)
                    value = config[line[start_index:end_index]]
                    line = line[:i] + value + line[end_index + 1 :]
                    i += len(value)
                    continue

                i += 1

            out_file.write(line)
