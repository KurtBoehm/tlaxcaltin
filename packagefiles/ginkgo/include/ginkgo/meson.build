# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

configure_file(
  input: 'config.hpp.in',
  output: 'config.hpp',
  configuration: cfg,
  format: 'cmake@',
)

configure_file(
  input: 'ginkgo.hpp.in',
  output: 'ginkgo.hpp',
  configuration: {'GKO_PUBLIC_HEADER_CONTENTS': gko_public_header_contents},
  format: 'cmake@',
)
