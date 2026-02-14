# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

amd_src = [
  'Source/amd_1.c',
  'Source/amd_2.c',
  'Source/amd_aat.c',
  'Source/amd_control.c',
  'Source/amd_defaults.c',
  'Source/amd_dump.c',
  'Source/amd_info.c',
  'Source/amd_order.c',
  'Source/amd_postorder.c',
  'Source/amd_post_tree.c',
  'Source/amd_preprocess.c',
  'Source/amd_valid.c',
  'Source/amd_l1.c',
  'Source/amd_l2.c',
  'Source/amd_l_aat.c',
  'Source/amd_l_control.c',
  'Source/amd_l_defaults.c',
  'Source/amd_l_dump.c',
  'Source/amd_l_info.c',
  'Source/amd_l_order.c',
  'Source/amd_l_postorder.c',
  'Source/amd_l_post_tree.c',
  'Source/amd_l_preprocess.c',
  'Source/amd_l_valid.c',
]

amd_inc = include_directories('Include')

amd_lib = shared_library(
  'amd',
  amd_src,
  dependencies: base_deps + [config_dep],
  include_directories: amd_inc,
  version: '3',
)

amd_dep = declare_dependency(
  link_with: amd_lib,
  dependencies: base_deps + [config_dep],
  include_directories: amd_inc,
  version: '3.3.4',
)
