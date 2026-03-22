# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# pkg-config support for GMock is in the master
# branch of the upstream repository.
# In order to be consistent with the upstream
# naming and the library conventions, the
# following changes have been made:
#
#   gmock_mainless_dep -> gmock_dep
#   gmock_with_main_dep -> gmock_main_dep
#
# Both GMock dependencies now include GTest,
# as this mimicks the same behavior as the
# upstream repo.

gmock_incdir = include_directories(
  'include',
  '.',
  is_system: true,
)

cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  gmock_lib = static_library(
    'gmock-all',
    files('../googletest/src/gtest-all.cc', 'src/gmock-all.cc'),
    include_directories: [gtest_incdir, gmock_incdir],
    override_options: override_cpp,
  )

  gmock_main_lib = static_library(
    'gmock_main',
    files(
      '../googletest/src/gtest-all.cc',
      'src/gmock-all.cc',
      'src/gmock_main.cc',
    ),
    include_directories: [gtest_incdir, gmock_incdir],
    override_options: override_cpp,
  )

  gmock_dep = declare_dependency(include_directories: [gtest_incdir, gmock_incdir], link_with: gmock_lib)

  gmock_main_dep = declare_dependency(
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: gmock_main_lib,
  )
else
  gmock_lib = library(
    'gmock-all',
    files('src/gmock-all.cc'),
    include_directories: [gtest_incdir, gmock_incdir],
    #can't do the following because of dllimport
    #dependencies: gtest_dep,
    dependencies: dependency('threads'),
    link_with: gtest_lib,
    override_options: override_cpp,
  )

  gmock_main_lib = library(
    'gmock_main',
    files('src/gmock_main.cc'),
    include_directories: [gtest_incdir, gmock_incdir],
    #can't do the following because of dllimport
    #dependencies: gtest_dep,
    link_with: [gtest_lib, gmock_lib],
    override_options: override_cpp,
  )

  gmock_dep = declare_dependency(
    include_directories: gmock_incdir,
    dependencies: gtest_dep,
    link_with: gmock_lib,
  )

  gmock_main_dep = declare_dependency(dependencies: gmock_dep, link_with: gmock_main_lib)
endif
