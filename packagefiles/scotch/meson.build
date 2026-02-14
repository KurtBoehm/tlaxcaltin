# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('Scotch', 'c', version: '7.0.11')

# C compiler arguments
c_args = []

scotch_version_long = meson.project_version()
scotch_version_parts = scotch_version_long.split('.')
scotch_version = scotch_version_parts[0]
scotch_release = scotch_version_parts[1]
scotch_patchlevel = scotch_version_parts[2]

c_args += [
  f'-DSCOTCH_VERSION_NUM=@scotch_version@',
  f'-DSCOTCH_RELEASE_NUM=@scotch_release@',
  f'-DSCOTCH_PATCHLEVEL_NUM=@scotch_patchlevel@',
]

subdir('src')
