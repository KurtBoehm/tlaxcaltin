# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project('SuiteSparse', 'c', 'cpp', version: '7.12.2')

cc = meson.get_compiler('c')
base_deps = [cc.find_library('m', required: false)]
has_posix_timers = cc.compiles(
  '''
  #include <unistd.h>
  int main() { return _POSIX_TIMERS; }
  ''',
)
clock_gettime_compiles = cc.links(
  '''
  #include <time.h>
  int main() {
    struct timespec res;
    return clock_gettime(CLOCK_REALTIME, &res);
  }
  ''',
)
if has_posix_timers and not clock_gettime_compiles
  base_deps += [cc.find_library('rt')]
endif

blas_dep = dependency('blas')
lapack_dep = dependency('lapack')
omp_dep = dependency('openmp')

subdir('SuiteSparse_config')
subdir('AMD')
subdir('BTF')
subdir('CAMD')
subdir('CCOLAMD')
subdir('COLAMD')
subdir('CHOLMOD')
subdir('CXSparse')
subdir('KLU')
subdir('LDL')
subdir('UMFPACK')
subdir('RBio')
subdir('SPQR')
