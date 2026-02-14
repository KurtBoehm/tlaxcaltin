# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'ParMETIS',
  'c',
)

include = include_directories('include')

m_dep = meson.get_compiler('c').find_library('m', required: false)
gklib_dep = subproject('gklib').get_variable('gklib_dep')
metis_dep = subproject('metis').get_variable('metis_dep')
mpi_dep = subproject('mpi-c').get_variable('mpi_dep')
assert(mpi_dep.found(), 'MPI not found!')

parmetis_lib = shared_library(
  'parmetis',
  [
    'libparmetis/akwayfm.c',
    'libparmetis/ametis.c',
    'libparmetis/balancemylink.c',
    'libparmetis/comm.c',
    'libparmetis/csrmatch.c',
    'libparmetis/ctrl.c',
    'libparmetis/debug.c',
    'libparmetis/diffutil.c',
    'libparmetis/frename.c',
    'libparmetis/gklib.c',
    'libparmetis/gkmetis.c',
    'libparmetis/gkmpi.c',
    'libparmetis/graph.c',
    'libparmetis/initbalance.c',
    'libparmetis/initmsection.c',
    'libparmetis/initpart.c',
    'libparmetis/kmetis.c',
    'libparmetis/kwayrefine.c',
    'libparmetis/match.c',
    'libparmetis/mdiffusion.c',
    'libparmetis/mesh.c',
    'libparmetis/mmetis.c',
    'libparmetis/move.c',
    'libparmetis/msetup.c',
    'libparmetis/node_refine.c',
    'libparmetis/ometis.c',
    'libparmetis/pspases.c',
    'libparmetis/redomylink.c',
    'libparmetis/remap.c',
    'libparmetis/renumber.c',
    'libparmetis/rmetis.c',
    'libparmetis/selectq.c',
    'libparmetis/serial.c',
    'libparmetis/stat.c',
    'libparmetis/timer.c',
    'libparmetis/util.c',
    'libparmetis/wave.c',
    'libparmetis/weird.c',
    'libparmetis/wspace.c',
    'libparmetis/xyzpart.c',
  ],
  c_args: ['-DIDXTYPEWIDTH=64', '-DREALTYPEWIDTH=64'],
  include_directories: [include, include_directories('libparmetis/')],
  dependencies: [gklib_dep, metis_dep, mpi_dep, m_dep],
)

parmetis_dep = declare_dependency(
  link_with: parmetis_lib,
  include_directories: include,
)
