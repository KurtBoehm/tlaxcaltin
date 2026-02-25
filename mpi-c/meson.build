# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('mpi-c', 'c')

impl = get_option('mpi_implementation')

if impl == 'openmpi'
  mpi_dep = dependency('ompi-c')
  mpi_implementation = 'openmpi'
elif impl == 'mpich'
  mpi_dep = dependency('mpich')
  mpi_implementation = 'mpich'
else
  mpi_dep = dependency('mpich', required: false)
  mpi_implementation = 'mpich'
  if not mpi_dep.found()
    mpi_dep = dependency('ompi-c')
    mpi_implementation = 'openmpi'
  endif
endif

prefix = mpi_dep.get_variable('prefix')
mpiexec = find_program(prefix / 'bin' / f'mpiexec@mpi_implementation@', required: false)
if not mpiexec.found()
  mpiexec = find_program(prefix / 'bin' / 'mpiexec')
endif
