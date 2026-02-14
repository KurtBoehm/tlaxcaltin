# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'combblas',
  'cpp',
  default_options: ['warning_level=1'],
)

src = [
  'src/CommGrid.cpp',
  'src/hash.cpp',
  'src/MemoryPool.cpp',
  'src/MPIOp.cpp',
  'src/MPIType.cpp',
]
inc = [
  include_directories('Applications/BipartiteMatchings'),
  include_directories('graph500-1.2/generator/include'),
  include_directories('include'),
  include_directories('psort-1.0/include'),
  include_directories('usort/include'),
]
mpi_dep = subproject('mpi-cpp').get_variable('mpi_dep')
assert(mpi_dep.found(), 'MPI not found!')
deps = [mpi_dep]

combblas_lib = shared_library(
  'combblas',
  src,
  include_directories: inc,
  dependencies: deps,
)
combblas_dep = declare_dependency(
  link_with: combblas_lib,
  include_directories: inc,
  dependencies: deps,
)
