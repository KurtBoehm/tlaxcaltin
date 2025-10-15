# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

iterator_test = {
  'iter.basic_iterator': files('basic_iterator.cpp'),
  'iter.diffmax_t': files('diffmax_t.cpp'),
  'iter.iterator': files('iterator.cpp'),
  'iter.common_iterator': files('common_iterator.cpp'),
  'iter.reverse_iterator': files('reverse_iterator.cpp'),
  'iter.unformatted_ostream_iterator': files('unformatted_ostream_iterator.cpp'),
  'iter.counted_iterator': files('counted_iterator.cpp'),
}

foreach name, sources : iterator_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    cpp_args: meson.get_compiler('cpp').get_supported_arguments('-Wno-incompatible-pointer-types', '/wd6011'),
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
