# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

ccolamd_src = [
  'Source/ccolamd.c',
  'Source/ccolamd_l.c',
]
ccolamd_inc = include_directories('Include')

ccolamd_lib = shared_library(
  'ccolamd',
  ccolamd_src,
  include_directories: ccolamd_inc,
  dependencies: base_deps + [config_dep],
  version: '3',
)

ccolamd_dep = declare_dependency(
  include_directories: ccolamd_inc,
  dependencies: base_deps + [config_dep],
  link_with: ccolamd_lib,
  version: '3.3.5',
)
