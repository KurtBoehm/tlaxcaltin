# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'arpackpp',
  'c',
  'cpp',
  default_options: ['cpp_std=c++17', 'warning_level=3'],
)

suitesparse = subproject('suitesparse')
arpackpp_dep = declare_dependency(
  dependencies: [
    dependency('blas'),
    dependency('arpack-ng'),
    dependency('lapack'),
    dependency('superlu'),
    suitesparse.get_variable('cholmod_dep'),
    suitesparse.get_variable('umfpack_dep'),
  ],
  include_directories: [include_directories('include')],
)

if get_option('examples')
  subdir('examples')
endif
