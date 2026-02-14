# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

colamd_src = [
  'Source/colamd.c',
  'Source/colamd_l.c',
]
colamd_inc = include_directories('Include')

colamd_lib = shared_library(
  'colamd',
  colamd_src,
  dependencies: base_deps + [config_dep],
  include_directories: colamd_inc,
  version: '3',
)

colamd_dep = declare_dependency(
  link_with: colamd_lib,
  include_directories: colamd_inc,
  dependencies: base_deps + [config_dep],
  version: '3.3.5',
)
