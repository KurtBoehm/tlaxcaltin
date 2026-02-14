# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

rbio_src = ['Source/RBio.c', 'Source/RBio_i.c']
rbio_inc = include_directories('Include')

rbio_lib = shared_library(
  'rbio',
  rbio_src,
  dependencies: base_deps + [config_dep],
  include_directories: rbio_inc,
  version: '4',
)

rbio_dep = declare_dependency(
  link_with: rbio_lib,
  include_directories: rbio_inc,
  dependencies: base_deps + [config_dep],
  version: '4.3.5',
)
