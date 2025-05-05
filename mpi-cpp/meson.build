# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('mpi-cpp', 'cpp')

impl = get_option('mpi_implementation')

if impl == 'openmpi'
  mpi_dep = dependency('ompi-cxx')
elif impl == 'mpich'
  mpi_dep = dependency('mpich')
else
  mpi_dep = dependency('mpich', required: false)
  if not mpi_dep.found()
    mpi_dep = dependency('ompi-cxx')
  endif
endif
prefix = mpi_dep.get_variable('prefix')
mpirun = find_program(prefix / 'bin' / 'mpirun')
