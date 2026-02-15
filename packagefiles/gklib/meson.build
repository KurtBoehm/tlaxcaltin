# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'GKlib',
  'c',
)

m_dep = meson.get_compiler('c').find_library('m', required: false)

gk_inc = include_directories('include')

gk_lib = shared_library(
  'GKlib',
  [
    'src/b64.c',
    'src/blas.c',
    'src/cache.c',
    'src/csr.c',
    'src/error.c',
    'src/evaluate.c',
    'src/fkvkselect.c',
    'src/fs.c',
    'src/getopt.c',
    'src/gkregex.c',
    'src/gk_util.c',
    'src/graph.c',
    'src/htable.c',
    'src/io.c',
    'src/itemsets.c',
    'src/mcore.c',
    'src/memory.c',
    'src/pqueue.c',
    'src/random.c',
    'src/rw.c',
    'src/seq.c',
    'src/sort.c',
    'src/string.c',
    'src/timers.c',
    'src/tokenizer.c',
  ],
  include_directories: [gk_inc],
  dependencies: [m_dep],
)

gklib_dep = declare_dependency(
  link_with: gk_lib,
  include_directories: gk_inc,
)
