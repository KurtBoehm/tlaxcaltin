# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'gtest',
  'cpp',
  version: '1.17.0',
  meson_version: '>=0.63.0',
  license: 'BSD-3-Clause',
)

if meson.version().version_compare('>=1.3.0')
  override_cpp = 'cpp_std=gnu++17,c++17'
else
  override_cpp = 'cpp_std=gnu++17'
endif

subdir('googletest')

subdir('googlemock')
