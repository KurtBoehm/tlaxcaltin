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
  dependencies: base_deps,
  include_directories: config_inc,
  version: '7',
)

config_dep = declare_dependency(
  link_with: config_lib,
  dependencies: base_deps,
  include_directories: config_inc,
  version: '7.12.2',
)
