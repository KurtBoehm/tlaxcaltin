# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('inotify-cpp', 'cpp', default_options: ['cpp_std=c++23'])

inc = include_directories('src/include')
inotify_cpp_lib = static_library(
  'inotify-cpp',
  [
    'src/Event.cpp',
    'src/FileSystemEvent.cpp',
    'src/Inotify.cpp',
    'src/Notification.cpp',
    'src/NotifierBuilder.cpp',
  ],
  include_directories: inc,
)
inotify_cpp_dep = declare_dependency(
  include_directories: inc,
  link_with: inotify_cpp_lib,
)
