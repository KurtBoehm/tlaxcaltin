# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

camd_src = [
  'Source/camd_1.c',
  'Source/camd_2.c',
  'Source/camd_aat.c',
  'Source/camd_control.c',
  'Source/camd_defaults.c',
  'Source/camd_dump.c',
  'Source/camd_info.c',
  'Source/camd_order.c',
  'Source/camd_postorder.c',
  'Source/camd_preprocess.c',
  'Source/camd_valid.c',
  'Source/camd_l1.c',
  'Source/camd_l2.c',
  'Source/camd_l_aat.c',
  'Source/camd_l_control.c',
  'Source/camd_l_defaults.c',
  'Source/camd_l_dump.c',
  'Source/camd_l_info.c',
  'Source/camd_l_order.c',
  'Source/camd_l_postorder.c',
  'Source/camd_l_preprocess.c',
  'Source/camd_l_valid.c',
]
camd_inc = include_directories('Include')

camd_lib = shared_library(
  'camd',
  camd_src,
  dependencies: base_deps + [config_dep],
  include_directories: camd_inc,
  version: '3',
)

camd_dep = declare_dependency(
  link_with: camd_lib,
  include_directories: camd_inc,
  dependencies: base_deps + [config_dep],
  version: '3.3.5',
)
