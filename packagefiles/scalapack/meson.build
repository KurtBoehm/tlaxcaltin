# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'ScaLAPACK',
  ['c', 'fortran'],
  version: '2.2.2',
  default_options: ['c_std=c17'],
)

scalapack_version = meson.project_version()
scalapack_version_split = scalapack_version.split('.')
scalapack_version_major = scalapack_version_split[0]
scalapack_version_minor = scalapack_version_split[1]
scalapack_version_patch = scalapack_version_split[2]

################################################################################
# Compiler and dependency discovery.
################################################################################

fc = meson.get_compiler('fortran')
cc = meson.get_compiler('c')

mpi_sub = subproject('mpi')
mpi_c_dep = mpi_sub.get_variable('mpi_c_dep')
mpi_f_dep = mpi_sub.get_variable('mpi_fortran_dep')

blas_dep = dependency('blas')
lapack_dep = dependency('lapack')

scalapack_deps = [mpi_c_dep, mpi_f_dep, lapack_dep, blas_dep]

################################################################################
# Compiler arguments
################################################################################

c_args = ['-Wno-error=implicit-function-declaration']

mangletest_lib = static_library('mangletest', 'TOOLS/mangletest.f90')

mangle_underscore_test = '''
extern void mangletest_(void);
int main(void) { mangletest_(); }
'''

mangle_uppercase_test = '''
extern void MANGLETEST(void);
int main(void) { MANGLETEST(); }
'''

if cc.compiles(mangle_underscore_test)
  message('Fortran mangling: underscore.')
  c_args += ['-DAdd_']
elif cc.compiles(mangle_uppercase_test)
  message('Fortran mangling: uppercase.')
  c_args += ['-DUpCase']
endif

fortran_no_implicit_args = fc.get_supported_arguments('-fno-implicit-none')

################################################################################
# Subdirectories
################################################################################

subdir('BLACS')
subdir('TOOLS')
subdir('PBLAS')
subdir('REDIST')
subdir('SRC')

################################################################################
# Library and dependency declaration
################################################################################

scalapack_lib = library(
  'scalapack',
  [
    blacs_srcs,
    tools_srcs,
    tools_c_srcs,
    pblas_srcs,
    pblas_f_srcs,
    ptzblas_srcs,
    ptools_srcs,
    pbblas_srcs,
    redist_srcs,
    src,
    src_c,
  ],
  dependencies: scalapack_deps,
  link_whole: [blacs_cint_lib],
  c_args: c_args,
  fortran_args: fortran_no_implicit_args,
  install: true,
  version: scalapack_version,
  soversion: f'@scalapack_version_major@.@scalapack_version_minor@',
)

scalapack_dep = declare_dependency(
  dependencies: scalapack_deps,
  link_with: scalapack_lib,
  version: scalapack_version,
)

################################################################################
# Testing.
################################################################################

# if build_tests
#   subdir('TESTING')
# endif
