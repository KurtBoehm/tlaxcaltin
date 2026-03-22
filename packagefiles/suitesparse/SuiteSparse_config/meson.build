# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

config_src = [
  'SuiteSparse_config.c',
]

config_inc = include_directories('.')

config_lib = shared_library(
  'suitesparseconfig',
  config_src,
  include_directories: config_inc,
  dependencies: base_deps,
  version: '7',
)

config_dep = declare_dependency(
  include_directories: config_inc,
  dependencies: base_deps,
  link_with: config_lib,
  version: '7.12.2',
)
