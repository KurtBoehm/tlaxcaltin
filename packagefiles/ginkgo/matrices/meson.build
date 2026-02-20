# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

configure_file(
  configuration: {'Ginkgo_BINARY_DIR': build_dir},
  input: 'config.hpp.in',
  output: 'config.hpp',
  format: 'cmake@',
)
subdir('test')
