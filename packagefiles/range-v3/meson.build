# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'range-v3',
  'cpp',
  version: '0.12.0',
  license: 'Boost, libc++, Stepanov and McJones "Elements of Programming", SGI STL',
)

range_inc = include_directories('include')

range_dep = declare_dependency(include_directories: range_inc)

if get_option('test')
  subdir('test')
endif
