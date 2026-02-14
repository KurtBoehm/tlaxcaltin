# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

spqr_src = [
  'Source/spqr_1colamd.cpp',
  'Source/spqr_1factor.cpp',
  'Source/spqr_1fixed.cpp',
  'Source/spqr_analyze.cpp',
  'Source/spqr_append.cpp',
  'Source/spqr_assemble.cpp',
  'Source/spqr_cholmod_wrappers.cpp',
  'Source/spqr_cpack.cpp',
  'Source/spqr_csize.cpp',
  'Source/spqr_cumsum.cpp',
  'Source/spqr_debug.cpp',
  'Source/spqr_factorize.cpp',
  'Source/spqr_fcsize.cpp',
  'Source/spqr_freefac.cpp',
  'Source/spqr_freenum.cpp',
  'Source/spqr_freesym.cpp',
  'Source/spqr_front.cpp',
  'Source/spqr_fsize.cpp',
  'Source/spqr_happly.cpp',
  'Source/spqr_happly_work.cpp',
  'Source/spqr_hpinv.cpp',
  'Source/spqr_kernel.cpp',
  'Source/spqr_larftb.cpp',
  'Source/spqr_maxcolnorm.cpp',
  'Source/spqr_panel.cpp',
  'Source/spqr_parallel.cpp',
  'Source/spqr_rconvert.cpp',
  'Source/spqr_rcount.cpp',
  'Source/spqr_rhpack.cpp',
  'Source/spqr_rmap.cpp',
  'Source/spqr_rsolve.cpp',
  'Source/spqr_shift.cpp',
  'Source/spqr_stranspose1.cpp',
  'Source/spqr_stranspose2.cpp',
  'Source/spqr_tol.cpp',
  'Source/spqr_trapezoidal.cpp',
  'Source/spqr_type.cpp',
  'Source/SuiteSparseQR_C.cpp',
  'Source/SuiteSparseQR.cpp',
  'Source/SuiteSparseQR_expert.cpp',
  'Source/SuiteSparseQR_qmult.cpp',
]
spqr_inc = include_directories('Include')

spqr_lib = shared_library(
  'spqr',
  spqr_src,
  dependencies: [
    config_dep,
    blas_dep,
    lapack_dep,
    amd_dep,
    cholmod_dep,
    colamd_dep,
  ],
  include_directories: spqr_inc,
  version: '4',
)

spqr_dep = declare_dependency(
  link_with: spqr_lib,
  include_directories: spqr_inc,
  dependencies: [
    config_dep,
    blas_dep,
    lapack_dep,
    amd_dep,
    cholmod_dep,
    colamd_dep,
  ],
  version: '4.3.6',
)
