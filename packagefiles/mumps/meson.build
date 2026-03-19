# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Based largely on https://github.com/scivision/mumps-superbuild

project('MUMPS', 'c', 'fortran', version: '5.8.2')

###########
# Options #
###########

build_double = get_option('build_double')
build_single = get_option('build_single')
build_complex = get_option('build_complex')
build_complex16 = get_option('build_complex16')
intsize64 = get_option('intsize64')

use_openmp = get_option('use_openmp')
use_scotch = get_option('use_scotch')
use_ptscotch = get_option('use_ptscotch')
use_metis = get_option('use_metis')
use_parmetis = get_option('use_parmetis')
use_scalapack = get_option('use_scalapack')

cc = meson.get_compiler('c')
fc = meson.get_compiler('fortran')
cc_gcc_compatible = ['gcc', 'clang'].contains(cc.get_id())

########################
# Common compile flags #
########################

mumps_cflags = ['-DAdd_']
mumps_fflags = []

if use_openmp and use_scotch
  mumps_cflags += ['-DMUMPS_SCOTCHIMPORTOMPTHREADS']
  mumps_fflags += ['-DMUMPS_SCOTCHIMPORTOMPTHREADS']
endif

if cc_gcc_compatible
  mumps_cflags += [
    '-Werror-implicit-function-declaration',
    '-fno-strict-aliasing',
  ]
  mumps_fflags += [
    '-fno-strict-aliasing',
    '-fimplicit-none',
    '-fallow-argument-mismatch',
    '-fallow-invalid-boz',
  ]
endif

if intsize64
  mumps_cflags += ['-DINTSIZE64', '-DPORD_INTSIZE64']
  if fc.get_id() == 'gcc'
    mumps_fflags += ['-fdefault-integer-8']
  endif
endif

#########################
# External dependencies #
#########################

mpi_sub = subproject('mpi')
mpi_c_dep = mpi_sub.get_variable('mpi_c_dep')
mpi_f_dep = mpi_sub.get_variable('mpi_fortran_dep')
threads_dep = dependency('threads')

if intsize64
  idx_type_width = 64
  lapack_dep = dependency('lapack64')
else
  idx_type_width = 32
  lapack_dep = dependency('lapack')
endif

if use_openmp
  openmp_f_dep = dependency('openmp', language: 'fortran')
else
  openmp_f_dep = []
endif

##############################
# mumps_int_def.h generation #
##############################

if intsize64
  int_def = 'src/mumps_int_def64_h.in'
else
  int_def = 'src/mumps_int_def32_h.in'
endif

configure_file(
  input: int_def,
  output: 'mumps_int_def.h',
  copy: true,
)

################
# PORD library #
################

pord_src = files(
  'PORD/lib/bucket.c',
  'PORD/lib/ddbisect.c',
  'PORD/lib/ddcreate.c',
  'PORD/lib/gbipart.c',
  'PORD/lib/gbisect.c',
  'PORD/lib/gelim.c',
  'PORD/lib/graph.c',
  'PORD/lib/interface.c',
  'PORD/lib/minpriority.c',
  'PORD/lib/multisector.c',
  'PORD/lib/nestdiss.c',
  'PORD/lib/sort.c',
  'PORD/lib/symbfac.c',
  'PORD/lib/tree.c',
)

pord_inc = include_directories('PORD/include')

pord_lib = library(
  'pord',
  pord_src,
  include_directories: pord_inc,
  c_args: mumps_cflags,
  pic: true,
)
pord_dep = declare_dependency(
  link_with: pord_lib,
  include_directories: pord_inc,
)

########################
# MUMPS common sources #
########################

comm_src_fortran = files(
  'src/ana_blk_m.F',
  'src/ana_omp_m.F',
  'src/ana_orderings_wrappers_m.F',
  'src/double_linked_list.F',
  'src/fac_asm_build_sort_index_ELT_m.F',
  'src/fac_asm_build_sort_index_m.F',
  'src/fac_descband_data_m.F',
  'src/fac_future_niv2_mod.F',
  'src/fac_maprow_data_m.F',
  'src/front_data_mgt_m.F',
  'src/lr_common.F',
  'src/lr_stats.F',
  'src/mumps_comm_buffer_common.F',
  'src/mumps_intr_types_common.F',
  'src/mumps_l0_omp_m.F',
  'src/mumps_load.F',
  'src/mumps_memory_mod.F',
  'src/mumps_mpitoomp_m.F',
  'src/mumps_ooc_common.F',
  'src/mumps_pivnul_mod.F',
  'src/mumps_static_mapping.F',
  'src/omp_tps_common_m.F',
  'src/sol_ds_common_m.F',
  'src/sol_omp_common_m.F',
  'src/tools_common_m.F',
)

comm_other_c = files(
  'src/mumps_addr.c',
  'src/mumps_common.c',
  'src/mumps_config_file_C.c',
  'src/mumps_flytes.c',
  'src/mumps_io.c',
  'src/mumps_io_basic.c',
  'src/mumps_io_err.c',
  'src/mumps_io_thread.c',
  'src/mumps_numa.c',
  'src/mumps_pord.c',
  'src/mumps_register_thread.c',
  'src/mumps_save_restore_C.c',
  'src/mumps_thread.c',
  'src/mumps_thread_affinity.c',
)

comm_other_fortran = files(
  'src/ana_AMDMF.F',
  'src/ana_blk.F',
  'src/ana_orderings.F',
  'src/ana_set_ordering.F',
  'src/bcast_errors.F',
  'src/estim_flops.F',
  'src/mumps_print_defined.F',
  'src/mumps_type2_blocking.F',
  'src/mumps_version.F',
  'src/sol_common.F',
  'src/tools_common.F',
)

##############################################
# Optional ordering packages in mumps_common #
##############################################

if use_scotch
  comm_other_c += files(
    'src/mumps_scotch.c',
    'src/mumps_scotch64.c',
    'src/mumps_scotch_int.c',
  )
endif

if use_metis or use_parmetis
  comm_other_c += files(
    'src/mumps_metis.c',
    'src/mumps_metis64.c',
    'src/mumps_metis_int.c',
  )
endif

###################
# GEMMT detection #
###################

have_dgemmt = false
have_sgemmt = false
have_cgemmt = false
have_zgemmt = false

num_prefixes = []

if build_double
  dgemmt_src = '''
program check
  use, intrinsic :: iso_fortran_env, only : real64
  implicit none
  external :: dgemmt
  real(real64), dimension(2,2) :: A, B, C
  CALL DGEMMT( 'U', 'N', 'T',  2 , 1 , 1._real64 , A , 2 , B , 2 , 1._real64 , C , 2 )
end program
'''
  have_dgemmt = fc.compiles(dgemmt_src, name: 'Check DGEMMT', dependencies: lapack_dep)
  num_prefixes += ['d']
endif

if build_single
  sgemmt_src = '''
program check
  use, intrinsic :: iso_fortran_env, only : real32
  implicit none
  external :: sgemmt
  real(real32), dimension(2,2) :: A, B, C
  CALL SGEMMT( 'U', 'N', 'T',  2 , 1 , 1._real32 , A , 2 , B , 2 , 1._real32 , C , 2 )
end program
'''
  have_sgemmt = fc.compiles(sgemmt_src, name: 'Check SGEMMT', dependencies: lapack_dep)
  num_prefixes += ['s']
endif

if build_complex
  cgemmt_src = '''
program check
  use, intrinsic :: iso_fortran_env, only : real32
  implicit none
  external :: cgemmt
  complex(real32), dimension(2,2) :: A, B, C
  CALL CGEMMT( 'U', 'N', 'T',  2 , 1 , 1._real32 , A , 2 , B , 2 , 1._real32 , C , 2 )
end program
'''
  have_cgemmt = fc.compiles(cgemmt_src, name: 'Check CGEMMT', dependencies: lapack_dep)
  num_prefixes += ['c']
endif

if build_complex16
  zgemmt_src = '''
program check
  use, intrinsic :: iso_fortran_env, only : real64
  implicit none
  external :: zgemmt
  complex(real64), dimension(2,2) :: A, B, C
  CALL ZGEMMT( 'U', 'N', 'T',  2 , 1 , 1._real64 , A , 2 , B , 2 , 1._real64 , C , 2 )
end program
'''
  have_zgemmt = fc.compiles(zgemmt_src, name: 'Check ZGEMMT', dependencies: lapack_dep)
  num_prefixes += ['z']
endif

blas_have_gemmt = have_sgemmt or have_dgemmt or have_cgemmt or have_zgemmt

#############################################
# Common dependencies and preprocessor defs #
#############################################

common_deps = [pord_dep, lapack_dep, threads_dep]
ordering_defs = ['-Dpord']

if use_metis
  common_deps += [dependency('metis')]
  ordering_defs += ['-Dmetis', '-DREALTYPEWIDTH=32', f'-DIDXTYPEWIDTH=@idx_type_width@']
endif
if use_parmetis
  assert(use_metis, '"use_parmetis" requires "use_metis"')
  common_deps += [dependency('parmetis')]
  ordering_defs += ['-Dparmetis']
endif

if use_scotch
  common_deps += [dependency('scotch'), dependency('scotcherr'), dependency('esmumps')]
  ordering_defs += ['-Dscotch']
endif
if use_ptscotch
  assert(use_scotch, '"use_ptscotch" requires "use_scotch"')
  common_deps += [dependency('ptscotch'), dependency('ptscotcherr'), dependency('ptesmumps')]
  ordering_defs += ['-Dptscotch']
endif

scalapack_defs = []
if use_scalapack
  common_deps += [dependency('scalapack')]
else
  scalapack_defs += ['-DNOSCALAPACK']
endif

gemmt_defs = []
if blas_have_gemmt
  gemmt_defs += ['-DGEMMT_AVAILABLE']
endif

################
# mumps_common #
################

inc_src = include_directories('src')
inc_pub = include_directories('include')

mumps_common_c = static_library(
  'mumps_common_c',
  comm_other_c,
  include_directories: [inc_src, inc_pub],
  dependencies: [mpi_c_dep, common_deps],
  c_args: [mumps_cflags, ordering_defs],
  pic: true,
)
mumps_common_fortran = static_library(
  'mumps_common_fortran',
  comm_src_fortran + comm_other_fortran,
  include_directories: [inc_src, inc_pub],
  dependencies: [mpi_f_dep, openmp_f_dep, common_deps],
  fortran_args: [mumps_fflags, ordering_defs, scalapack_defs, gemmt_defs],
  pic: true,
)

mumps_common_lib = library(
  'mumps_common',
  link_whole: [mumps_common_c, mumps_common_fortran],
  include_directories: [inc_src, inc_pub],
  dependencies: [mpi_c_dep, mpi_f_dep, openmp_f_dep, common_deps],
  version: meson.project_version(),
)
mumps_common_dep = declare_dependency(
  link_with: [mumps_common_lib],
  include_directories: inc_pub,
  dependencies: [mpi_c_dep, mpi_f_dep, openmp_f_dep, common_deps],
  version: meson.project_version(),
)

################################
# Precision-specific libraries #
################################

a_mumps_libs = []
foreach a : num_prefixes
  src_fortran = files(
    f'src/@a@ana_aux.F',
    f'src/@a@ana_aux_ELT.F',
    f'src/@a@ana_aux_par.F',
    f'src/@a@ana_dist_m.F',
    f'src/@a@ana_driver.F',
    f'src/@a@ana_LDLT_preprocess.F',
    f'src/@a@ana_lr.F',
    f'src/@a@ana_mtrans.F',
    f'src/@a@ana_reordertree.F',
    f'src/@a@arrowheads.F',
    f'src/@a@bcast_int.F',
    f'src/@a@end_driver.F',
    f'src/@a@fac_asm.F',
    f'src/@a@fac_asm_ELT.F',
    f'src/@a@fac_asm_master_ELT_m.F',
    f'src/@a@fac_asm_master_m.F',
    f'src/@a@fac_b.F',
    f'src/@a@fac_compact_factors_m.F',
    f'src/@a@fac_determinant.F',
    f'src/@a@fac_diag.F',
    f'src/@a@fac_distrib_distentry.F',
    f'src/@a@fac_distrib_ELT.F',
    f'src/@a@fac_dist_arrowheads_omp.F',
    f'src/@a@fac_driver.F',
    f'src/@a@fac_front_aux.F',
    f'src/@a@fac_front_LDLT_type1.F',
    f'src/@a@fac_front_LDLT_type2.F',
    f'src/@a@fac_front_LU_type1.F',
    f'src/@a@fac_front_LU_type2.F',
    f'src/@a@fac_front_type2_aux.F',
    f'src/@a@fac_lastrtnelind.F',
    f'src/@a@fac_lr.F',
    f'src/@a@fac_mem_alloc_cb.F',
    f'src/@a@fac_mem_compress_cb.F',
    f'src/@a@fac_mem_dynamic.F',
    f'src/@a@fac_mem_free_block_cb.F',
    f'src/@a@fac_mem_stack.F',
    f'src/@a@fac_mem_stack_aux.F',
    f'src/@a@fac_omp_m.F',
    f'src/@a@fac_par_m.F',
    f'src/@a@fac_process_band.F',
    f'src/@a@fac_process_bf.F',
    f'src/@a@fac_process_blfac_slave.F',
    f'src/@a@fac_process_blocfacto.F',
    f'src/@a@fac_process_blocfacto_LDLT.F',
    f'src/@a@fac_process_contrib_type1.F',
    f'src/@a@fac_process_contrib_type2.F',
    f'src/@a@fac_process_contrib_type3.F',
    f'src/@a@fac_process_end_facto_slave.F',
    f'src/@a@fac_process_maprow.F',
    f'src/@a@fac_process_master2.F',
    f'src/@a@fac_process_message.F',
    f'src/@a@fac_process_root2slave.F',
    f'src/@a@fac_process_root2son.F',
    f'src/@a@fac_process_rtnelind.F',
    f'src/@a@fac_root_parallel.F',
    f'src/@a@fac_scalings.F',
    f'src/@a@fac_scalings_simScaleAbs.F',
    f'src/@a@fac_scalings_simScale_util.F',
    f'src/@a@fac_sispointers_m.F',
    f'src/@a@fac_sol_l0omp_m.F',
    f'src/@a@fac_sol_pool.F',
    f'src/@a@fac_type3_symmetrize.F',
    f'src/@a@ini_defaults.F',
    f'src/@a@ini_driver.F',
    f'src/@a@lr_core.F',
    f'src/@a@lr_type.F',
    f'src/@a@mumps_comm_buffer.F',
    f'src/@a@mumps_config_file.F',
    f'src/@a@mumps_driver.F',
    f'src/@a@mumps_f77.F',
    f'src/@a@mumps_intr_types.F',
    f'src/@a@mumps_iXamax.F',
    f'src/@a@mumps_lr_data_m.F',
    f'src/@a@mumps_mpi3_mod.F',
    f'src/@a@mumps_ooc.F',
    f'src/@a@mumps_ooc_buffer.F',
    f'src/@a@mumps_save_restore.F',
    f'src/@a@mumps_save_restore_files.F',
    f'src/@a@mumps_sol_es.F',
    f'src/@a@mumps_struc_def.F',
    f'src/@a@ooc_panel_piv.F',
    f'src/@a@omp_tps_m.F',
    f'src/@a@rank_revealing.F',
    f'src/@a@sol_aux.F',
    f'src/@a@sol_bwd.F',
    f'src/@a@sol_bwd_aux.F',
    f'src/@a@sol_c.F',
    f'src/@a@sol_distrhs.F',
    f'src/@a@sol_distsol.F',
    f'src/@a@sol_driver.F',
    f'src/@a@sol_fwd.F',
    f'src/@a@sol_fwd_aux.F',
    f'src/@a@sol_lr.F',
    f'src/@a@sol_matvec.F',
    f'src/@a@sol_omp_m.F',
    f'src/@a@sol_root_parallel.F',
    f'src/@a@static_ptr_m.F',
    f'src/@a@tools.F',
    f'src/@a@type3_root.F',
  )
  src_c = files(f'src/@a@mumps_gpu.c')
  cint_src = files('src/mumps_c.c')

  # Per-precision definitions
  a_defs = [ordering_defs, f'-DMUMPS_ARITH=MUMPS_ARITH_@a@']

  # GEMMT_AVAILABLE only where the BLAS symbol exists
  a_gemmt_defs = []
  if {'s': have_sgemmt, 'd': have_dgemmt, 'c': have_cgemmt, 'z': have_zgemmt}[a]
    a_gemmt_defs += ['-DGEMMT_AVAILABLE']
  endif

  a_mumps_c_lib = static_library(
    f'@a@mumps_c',
    [cint_src, src_c],
    c_args: [mumps_cflags, a_defs],
    include_directories: inc_pub,
    dependencies: [mpi_c_dep, mumps_common_dep],
    pic: true,
  )
  a_mumps_f_lib = static_library(
    f'@a@mumps_fortran',
    src_fortran,
    fortran_args: [mumps_fflags, a_defs, scalapack_defs, a_gemmt_defs],
    include_directories: [inc_src, inc_pub],
    dependencies: [mpi_f_dep, openmp_f_dep, mumps_common_dep],
    pic: true,
  )

  a_mumps_lib = library(
    f'@a@mumps',
    link_whole: [a_mumps_c_lib, a_mumps_f_lib],
    dependencies: [mpi_f_dep, openmp_f_dep],
    version: meson.project_version(),
  )
  a_mumps_libs += [a_mumps_c_lib, a_mumps_f_lib]
endforeach

###########################
# Aggregate MUMPS library #
###########################

mumps_lib = library(
  'mumps',
  link_whole: a_mumps_libs,
  dependencies: [mpi_f_dep, openmp_f_dep],
  version: meson.project_version(),
)
mumps_dep = declare_dependency(
  link_with: mumps_lib,
  include_directories: inc_pub,
  dependencies: [mpi_c_dep, mpi_f_dep, openmp_f_dep, common_deps],
  version: meson.project_version(),
)
