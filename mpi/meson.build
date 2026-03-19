# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('mpi')

impl = get_option('mpi_implementation')

if impl == 'openmpi'
  mpi_c_dep = dependency('ompi-c')
  mpi_cpp_dep = dependency('ompi-cxx')
  mpi_fortran_dep = dependency('ompi-fort')
  mpi_implementation = 'openmpi'
elif impl == 'mpich'
  mpi_c_dep = dependency('mpich')
  mpi_cpp_dep = mpi_c_dep
  mpifort = mpi_c_dep.get_variable('prefix') / 'lib' / 'libmpifort.so'
  mpi_fortran_dep = [mpi_c_dep, declare_dependency(link_args: mpifort)]
  mpi_implementation = 'mpich'
else
  mpi_c_dep = dependency('mpich', required: false)
  mpi_implementation = 'mpich'
  if not mpi_c_dep.found()
    mpi_c_dep = dependency('ompi-c')
    mpi_cpp_dep = dependency('ompi-cxx')
    mpi_fortran_dep = dependency('ompi-fort')
    mpi_implementation = 'openmpi'
  else
    mpi_cpp_dep = mpi_c_dep
    mpifort = mpi_c_dep.get_variable('prefix') / 'lib' / 'libmpifort.so'
    mpi_fortran_dep = [mpi_c_dep, declare_dependency(link_args: mpifort)]
  endif
endif

prefix = mpi_c_dep.get_variable('prefix')
mpiexec = find_program(prefix / 'bin' / f'mpiexec.@mpi_implementation@', required: false)
if not mpiexec.found()
  mpiexec = find_program(prefix / 'bin' / 'mpiexec')
endif
