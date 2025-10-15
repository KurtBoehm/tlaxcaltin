# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Iterable
from pathlib import Path
from typing import Final


header: Final = """# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""


def iterdir_recursive(p: Path) -> Iterable[Path]:
    if p.is_dir():
        for child in sorted(p.iterdir()):
            yield from iterdir_recursive(child)
    else:
        yield p


base = Path(__file__).parents[1]
for p in iterdir_recursive(base):
    if p.suffix != ".wrap" and p.name not in ["meson.build", "meson_options.txt"]:
        continue
    with open(p, "r") as f:
        txt = f.read()
    if txt.startswith(header):
        continue
    with open(p, "w") as f:
        f.write(header + "\n" + txt)
