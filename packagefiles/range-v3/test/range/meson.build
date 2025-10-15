# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

range_test = {
  'range.access': files('access.cpp'),
  'range.conversion': files('conversion.cpp'),
  'range.index': files('index.cpp'),
  'range.operations': files('operations.cpp'),
}

foreach name, sources : range_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
