# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'METIS',
  'c',
)

include = include_directories('include')

gklib_dep = subproject('gklib').get_variable('gklib_dep')
m_dep = meson.get_compiler('c').find_library('m', required: false)
deps = [gklib_dep, m_dep]

metis_lib = shared_library(
  'metis',
  [
    'libmetis/auxapi.c',
    'libmetis/balance.c',
    'libmetis/bucketsort.c',
    'libmetis/checkgraph.c',
    'libmetis/coarsen.c',
    'libmetis/compress.c',
    'libmetis/contig.c',
    'libmetis/debug.c',
    'libmetis/fm.c',
    'libmetis/fortran.c',
    'libmetis/frename.c',
    'libmetis/gklib.c',
    'libmetis/graph.c',
    'libmetis/initpart.c',
    'libmetis/kmetis.c',
    'libmetis/kwayfm.c',
    'libmetis/kwayrefine.c',
    'libmetis/mcutil.c',
    'libmetis/mesh.c',
    'libmetis/meshpart.c',
    'libmetis/minconn.c',
    'libmetis/mincover.c',
    'libmetis/mmd.c',
    'libmetis/ometis.c',
    'libmetis/options.c',
    'libmetis/parmetis.c',
    'libmetis/pmetis.c',
    'libmetis/refine.c',
    'libmetis/separator.c',
    'libmetis/sfm.c',
    'libmetis/srefine.c',
    'libmetis/stat.c',
    'libmetis/timing.c',
    'libmetis/util.c',
    'libmetis/wspace.c',
  ],
  include_directories: [include, include_directories('libmetis/')],
  dependencies: deps,
)

metis_dep = declare_dependency(
  link_with: metis_lib,
  include_directories: include,
  dependencies: deps,
)
