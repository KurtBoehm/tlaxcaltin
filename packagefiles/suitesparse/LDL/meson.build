# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

ldl_src = [
  'Source/ldl.c',
  'Source/ldll.c',
]
ldl_inc = include_directories('Include')

ldl_lib = shared_library(
  'ldl',
  ldl_src,
  include_directories: ldl_inc,
  dependencies: base_deps + [config_dep],
  version: '3',
)

ldl_dep = declare_dependency(
  include_directories: ldl_inc,
  dependencies: base_deps + [config_dep],
  link_with: ldl_lib,
  version: '3.3.3',
)
