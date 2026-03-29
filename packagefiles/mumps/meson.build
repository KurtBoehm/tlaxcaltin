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

parallel = get_option('mpi_implementation') != 'none'

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

if not parallel
  if use_ptscotch
    warning('PT-Scotch is disabled in a non-MPI build.')
    use_ptscotch = false
  endif
  if use_parmetis
    warning('ParMETIS is disabled in a non-MPI build.')
    use_parmetis = false
  endif
  if use_scalapack
    warning('ScaLAPACK is disabled in a non-MPI build.')
    use_scalapack = false
  endif
endif

cc = meson.get_compiler('c')
fc = meson.get_compiler('fortran')

cc_gcc_compatible = ['gcc', 'clang'].contains(cc.get_id())
fc_gcc_compatible = ['gcc', 'llvm-flang'].contains(fc.get_id())

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
endif

if fc_gcc_compatible
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

threads_dep = dependency('threads')

# Sequential backend: libseq
libseq_inc = include_directories('libseq')

libseq_c_lib = static_library(
  'mpiseq_c',
  files('libseq/elapse.c', 'libseq/mpic.c'),
  include_directories: libseq_inc,
  pic: true,
  c_args: mumps_cflags,
)

libseq_f_lib = static_library(
  'mpiseq_fortran',
  files('libseq/mpi.f'),
  include_directories: libseq_inc,
  link_with: libseq_c_lib,
  override_options: ['warning_level=0'],
  pic: true,
  fortran_args: mumps_fflags,
)

mpi_c_dep_seq = declare_dependency(
  include_directories: libseq_inc,
  link_with: libseq_c_lib,
)
mpi_f_dep_seq = declare_dependency(
  include_directories: libseq_inc,
  link_with: libseq_f_lib,
)

# Parallel backend: real MPI
if parallel
  mpi_sub = subproject('mpi')
  mpi_c_dep_par = mpi_sub.get_variable('mpi_c_dep')
  mpi_f_dep_par = mpi_sub.get_variable('mpi_fortran_dep')
endif

##########
# LAPACK #
##########

if intsize64
  idx_type_width = 64
  lapack_dep = dependency('lapack64')
else
  idx_type_width = 32
  lapack_dep = dependency('lapack')
endif

##########
# OpenMP #
##########

openmp_f_dep = use_openmp ? dependency('openmp', language: 'fortran') : []

##############################
# mumps_int_def.h generation #
##############################

int_def = intsize64 ? 'src/mumps_int_def64_h.in' : 'src/mumps_int_def32_h.in'

configure_file(
  input: int_def,
  output: 'mumps_int_def.h',
  copy: true,
  build_subdir: 'gen_defs',
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
  pic: true,
  c_args: mumps_cflags,
)
pord_dep = declare_dependency(include_directories: pord_inc, link_with: pord_lib)

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

gemmt_test = '''
program check
  use, intrinsic :: iso_fortran_env, only : @0@
  implicit none
  external :: @1@
  @2@, dimension(2,2) :: A, B, C
  CALL @1@( 'U', 'N', 'T', 2, 1, 1._@0@, A, 2, B, 2, 1._@0@, C, 2 )
end program
'''

have_sgemmt = false
have_dgemmt = false
have_cgemmt = false
have_zgemmt = false
num_prefixes = []

if build_double
  src = gemmt_test.format('real64', 'dgemmt', 'real(real64)')
  have_dgemmt = fc.compiles(src, name: 'Check DGEMMT', dependencies: lapack_dep)
  num_prefixes += ['d']
endif

if build_single
  src = gemmt_test.format('real32', 'sgemmt', 'real(real32)')
  have_sgemmt = fc.compiles(src, name: 'Check SGEMMT', dependencies: lapack_dep)
  num_prefixes += ['s']
endif

if build_complex
  src = gemmt_test.format('real32', 'cgemmt', 'complex(real32)')
  have_cgemmt = fc.compiles(src, name: 'Check CGEMMT', dependencies: lapack_dep)
  num_prefixes += ['c']
endif

if build_complex16
  src = gemmt_test.format('real64', 'zgemmt', 'complex(real64)')
  have_zgemmt = fc.compiles(src, name: 'Check ZGEMMT', dependencies: lapack_dep)
  num_prefixes += ['z']
endif

blas_have_gemmt = have_sgemmt or have_dgemmt or have_cgemmt or have_zgemmt
have_gemmt_map = {'s': have_sgemmt, 'd': have_dgemmt, 'c': have_cgemmt, 'z': have_zgemmt}

#############################################
# Common dependencies and preprocessor defs #
#############################################

common_deps = [pord_dep, lapack_dep, threads_dep]
common_deps_par = []
common_defs = ['-Dpord']
common_defs_par = []

if use_metis
  common_deps += [dependency('metis')]
  common_defs += ['-Dmetis', '-DREALTYPEWIDTH=32', f'-DIDXTYPEWIDTH=@idx_type_width@']
endif

if use_parmetis
  assert(use_metis, '"use_parmetis" requires "use_metis"')
  common_deps_par += [dependency('parmetis')]
  common_defs_par += ['-Dparmetis']
endif

if use_scotch
  common_deps += [dependency('scotch'), dependency('scotcherr'), dependency('esmumps')]
  common_defs += ['-Dscotch']
endif

if use_ptscotch
  assert(use_scotch, '"use_ptscotch" requires "use_scotch"')
  common_deps_par += [dependency('ptscotch'), dependency('ptscotcherr'), dependency('ptesmumps')]
  common_defs_par += ['-Dptscotch']
endif

if use_scalapack
  common_deps_par += [dependency('scalapack')]
else
  common_defs_par += ['-DNOSCALAPACK']
endif

common_deps_par = common_deps + common_deps_par

################
# mumps_common #
################

inc_src = include_directories('src')
inc_pub = [include_directories('include'), include_directories('gen_defs')]

mumps_common_build = [
  {
    'name_suffix': 'seq',
    'mpi_c_dep': mpi_c_dep_seq,
    'mpi_f_dep': mpi_f_dep_seq,
    'common_deps': common_deps,
    'common_defs': common_defs,
  },
]

if parallel
  mumps_common_build += [
    {
      'name_suffix': 'par',
      'mpi_c_dep': mpi_c_dep_par,
      'mpi_f_dep': mpi_f_dep_par,
      'common_deps': common_deps_par,
      'common_defs': common_defs + common_defs_par,
    },
  ]
endif

mumps_common_libs = {}

foreach cfg : mumps_common_build
  name_suffix = cfg['name_suffix']
  mpi_c_dep = cfg['mpi_c_dep']
  mpi_f_dep = cfg['mpi_f_dep']
  common_deps_cur = cfg['common_deps']
  common_defs_cur = cfg['common_defs']

  mumps_common_c = static_library(
    f'mumps_common_c_@name_suffix@',
    comm_other_c,
    include_directories: [inc_src, inc_pub],
    dependencies: [mpi_c_dep, common_deps_cur],
    pic: true,
    c_args: [mumps_cflags, common_defs_cur],
  )

  gemmt_defs = blas_have_gemmt ? ['-DGEMMT_AVAILABLE'] : []

  mumps_common_fortran = static_library(
    f'mumps_common_fortran_@name_suffix@',
    [comm_src_fortran, comm_other_fortran],
    include_directories: [inc_src, inc_pub],
    dependencies: [mpi_f_dep, openmp_f_dep, common_deps_cur],
    override_options: ['warning_level=0'],
    pic: true,
    fortran_args: [mumps_fflags, common_defs_cur, gemmt_defs],
  )

  mumps_common_lib = static_library(
    f'mumps_common_@name_suffix@',
    include_directories: [inc_src, inc_pub],
    dependencies: [mpi_c_dep, mpi_f_dep, openmp_f_dep, common_deps_cur],
    link_whole: [mumps_common_c, mumps_common_fortran],
  )

  mumps_common_libs += {name_suffix: mumps_common_lib}
endforeach

mumps_common_lib_seq = mumps_common_libs['seq']
if parallel
  mumps_common_lib_par = mumps_common_libs['par']
endif

################################
# Precision-specific libraries #
################################

a_mumps_libs_seq = []
a_mumps_libs_par = []

cint_src = files('src/mumps_c.c')

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

  a_defs_base = [common_defs, f'-DMUMPS_ARITH=MUMPS_ARITH_@a@']

  a_gemmt_defs = have_gemmt_map[a] ? ['-DGEMMT_AVAILABLE'] : []

  # Sequential variant (libseq, no ScaLAPACK)
  a_mumps_c_lib_seq = static_library(
    f'@a@mumps_c_seq',
    [cint_src, src_c],
    include_directories: inc_pub,
    dependencies: [common_deps],
    link_with: [mumps_common_lib_seq],
    pic: true,
    c_args: [mumps_cflags, a_defs_base],
  )

  a_mumps_f_lib_seq = static_library(
    f'@a@mumps_fortran_seq',
    src_fortran,
    include_directories: [inc_src, inc_pub],
    dependencies: [mpi_f_dep_seq, openmp_f_dep, common_deps],
    link_with: [mumps_common_lib_seq],
    override_options: ['warning_level=0'],
    pic: true,
    fortran_args: [mumps_fflags, a_defs_base, ['-DNOSCALAPACK'], a_gemmt_defs],
  )

  a_mumps_libs_seq += [a_mumps_c_lib_seq, a_mumps_f_lib_seq]

  if parallel
    # Parallel variant (real MPI, optional ScaLAPACK)
    a_defs_par = [a_defs_base, common_defs_par]

    scalapack_defs_par = use_scalapack ? [] : ['-DNOSCALAPACK']

    a_mumps_c_lib_par = static_library(
      f'@a@mumps_c_par',
      [cint_src, src_c],
      include_directories: inc_pub,
      dependencies: [mpi_c_dep_par, common_deps_par],
      link_with: [mumps_common_lib_par],
      pic: true,
      c_args: [mumps_cflags, a_defs_par],
    )

    a_mumps_f_lib_par = static_library(
      f'@a@mumps_fortran_par',
      src_fortran,
      include_directories: [inc_src, inc_pub],
      dependencies: [mpi_f_dep_par, openmp_f_dep, common_deps_par],
      link_with: [mumps_common_lib_par],
      override_options: ['warning_level=0'],
      pic: true,
      fortran_args: [mumps_fflags, a_defs_par, scalapack_defs_par, a_gemmt_defs],
    )

    a_mumps_libs_par += [a_mumps_c_lib_par, a_mumps_f_lib_par]
  endif
endforeach

###########################
# Aggregate MUMPS library #
###########################

mumps_lib_seq = library(
  'mumps_seq',
  dependencies: [mpi_f_dep_seq, openmp_f_dep],
  link_with: [mumps_common_lib_seq],
  link_whole: a_mumps_libs_seq,
  version: meson.project_version(),
)

mumps_dep_seq = declare_dependency(
  include_directories: inc_pub,
  dependencies: [mpi_c_dep_seq, mpi_f_dep_seq, openmp_f_dep, common_deps],
  link_with: [mumps_lib_seq, mumps_common_lib_seq],
  version: meson.project_version(),
)

meson.override_dependency('mumps_seq', mumps_dep_seq)

if parallel
  mumps_lib_par = library(
    'mumps_par',
    dependencies: [mpi_f_dep_par, openmp_f_dep, common_deps],
    link_with: [mumps_common_lib_par],
    link_whole: a_mumps_libs_par,
    version: meson.project_version(),
  )

  mumps_dep_par = declare_dependency(
    include_directories: inc_pub,
    dependencies: [mpi_c_dep_par, mpi_f_dep_par, openmp_f_dep, common_deps_par],
    link_with: [mumps_lib_par, mumps_common_lib_par],
    version: meson.project_version(),
  )

  meson.override_dependency('mumps_par', mumps_dep_par)
endif

########################
# Hybrid MUMPS library #
########################

mumps_hybrid_seq_map = meson.current_source_dir() + '/hybrid/src/mumps-seq.map'
mumps_hybrid_seq_lib = shared_library(
  'mumps_hybrid_seq',
  'hybrid/src/mumps-seq.c',
  include_directories: [inc_pub, 'hybrid/include'],
  dependencies: [openmp_f_dep, common_deps],
  link_whole: [libseq_f_lib, a_mumps_libs_seq, mumps_common_lib_seq],
  link_args: [f'-Wl,--version-script=@mumps_hybrid_seq_map@'],
  version: meson.project_version(),
)

if parallel
  mumps_hybrid_par_map = meson.current_source_dir() + '/hybrid/src/mumps-par.map'
  mumps_hybrid_par_lib = shared_library(
    'mumps_hybrid_par',
    'hybrid/src/mumps-par.c',
    include_directories: [inc_pub, 'hybrid/include'],
    dependencies: [mpi_f_dep_par, openmp_f_dep, common_deps_par],
    link_whole: [a_mumps_libs_par, mumps_common_lib_par],
    link_args: [f'-Wl,--version-script=@mumps_hybrid_par_map@'],
    version: meson.project_version(),
  )

  mumps_hybrid_dep = declare_dependency(
    include_directories: [inc_pub, 'hybrid/include'],
    dependencies: [mpi_f_dep_par, openmp_f_dep, common_deps_par],
    link_with: [mumps_hybrid_seq_lib, mumps_hybrid_par_lib],
    version: meson.project_version(),
  )
else
  # Hybrid build without MPI: only the sequential side
  mumps_hybrid_dep = declare_dependency(
    include_directories: [inc_pub, 'hybrid/include'],
    dependencies: [openmp_f_dep, common_deps],
    link_with: [mumps_hybrid_seq_lib],
    version: meson.project_version(),
  )
endif

meson.override_dependency('mumps_hybrid', mumps_hybrid_dep)
