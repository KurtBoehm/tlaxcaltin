# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

btf_src = [
  'Source/btf_maxtrans.c',
  'Source/btf_order.c',
  'Source/btf_strongcomp.c',
  'Source/btf_l_maxtrans.c',
  'Source/btf_l_order.c',
  'Source/btf_l_strongcomp.c',
]
btf_inc = include_directories('Include')

btf_lib = shared_library(
  'btf',
  btf_src,
  include_directories: btf_inc,
  dependencies: base_deps + [config_dep],
  version: '2',
)

btf_dep = declare_dependency(
  include_directories: btf_inc,
  dependencies: base_deps + [config_dep],
  link_with: btf_lib,
  version: '2.3.3',
)
