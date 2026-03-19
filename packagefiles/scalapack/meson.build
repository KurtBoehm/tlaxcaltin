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

build_tests = get_option('test')

fc = meson.get_compiler('fortran')
cc = meson.get_compiler('c')

mpi_c_dep = subproject('mpi').get_variable('mpi_c_dep')
mpi_f_dep = subproject('mpi').get_variable('mpi_fortran_dep')
blas_dep = dependency('blas')
lapack_dep = dependency('lapack')

c_args = ['-Wno-error=implicit-function-declaration']

mangletest_lib = static_library('mangletest', 'TOOLS/mangletest.f90')
if cc.compiles('extern void mangletest_(void); int main(void) { mangletest_(); }')
  message('Fortran mangling: underscore')
  c_args += ['-DAdd_']
elif cc.compiles('extern void MANGLETEST(void); int main(void) { MANGLETEST(); }')
  message('Fortran mangling: uppercase')
  c_args += ['-DUpCase']
endif

subdir('BLACS')
subdir('TOOLS')
subdir('PBLAS')
subdir('REDIST')
subdir('SRC')

# Single library containing both C and Fortran sources
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
  c_args: c_args,
  dependencies: [mpi_c_dep, mpi_f_dep, lapack_dep, blas_dep],
  link_whole: [blacs_cint_lib],
  version: scalapack_version,
  soversion: f'@scalapack_version_major@.@scalapack_version_minor@',
  install: true,
)
scalapack_dep = declare_dependency(
  link_with: scalapack_lib,
  dependencies: [mpi_c_dep, mpi_f_dep, lapack_dep, blas_dep],
  version: scalapack_version,
)

# if build_tests
#   subdir('TESTING')
# endif
