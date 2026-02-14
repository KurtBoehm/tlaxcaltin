# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

name_suffix = get_option('name_suffix')
scotch_deterministic = get_option('scotch_deterministic')

libscotch_inc = [include_directories('.')]

dummysizes_exe = executable(
  'dummysizes',
  'dummysizes.c',
  c_args: c_args,
)
scotch_h_gen = custom_target(
  'scotch_h',
  input: ['library.h'],
  output: ['scotch.h'],
  command: [dummysizes_exe, '-s' + name_suffix, '@INPUT@', '@OUTPUT@'],
  build_by_default: true,
)
scotchf_h_gen = custom_target(
  'scotchf_h',
  input: ['library_f.h'],
  output: ['scotch_f.h'],
  command: [dummysizes_exe, '-s' + name_suffix, '@INPUT@', '@OUTPUT@'],
  build_by_default: true,
)

ptdummysizes_exe = []
ptscotch_h_gen   = []
ptscotchf_h_gen  = []
if build_ptscotch
  ptdummysizes_exe = executable(
    'ptdummysizes',
    'dummysizes.c',
    c_args: c_args + ['-DSCOTCH_PTSCOTCH'],
    dependencies: [mpi_dep],
  )
  ptscotch_h_gen = custom_target(
    'ptscotch_h',
    input: ['library_pt.h'],
    output: ['ptscotch.h'],
    command: [ptdummysizes_exe, '-s' + name_suffix, '@INPUT@', '@OUTPUT@'],
    build_by_default: true,
  )

  ptscotchf_h_gen = custom_target(
    'ptscotchf_h',
    input: ['library_pt_f.h'],
    output: ['ptscotchf.h'],
    command: [ptdummysizes_exe, '-s' + name_suffix, '@INPUT@', '@OUTPUT@'],
    build_by_default: true,
  )
endif

# Generate using Bison and Flex
parser_yy_gen = []
parser_ll_gen = []
if bison_prg.found() and flex_prg.found()
  parser_yy_gen = custom_target(
    'parser_yy',
    input: ['parser_yy.y'],
    output: ['parser_ly.h', 'parser_yy.c'],
    command: [
      bison_prg,
      f'-p_SCOTCHyy@name_suffix@',
      '--defines=@OUTPUT0@',
      '--output=@OUTPUT1@',
      '@INPUT@',
    ],
    build_by_default: true,
  )
  parser_ll_gen = custom_target(
    'parser_ll',
    input: ['parser_ll.l'],
    output: ['parser_lh.h', 'parser_ll.c'],
    command: [
      flex_prg,
      f'-P_SCOTCHyy@name_suffix@',
      '--header-file=@OUTPUT0@',
      '--outfile=@OUTPUT1@',
      '@INPUT@',
    ],
    build_by_default: true,
  )
else
  parser_yy_gen = files('last_resort/parser_yy.c')
  parser_ll_gen = files('last_resort/parser_ll.c')
  libscotch_inc += include_directories('last_resort')
endif

scotch_src = [
  files(
    'arch.c',
    'arch_build.c',
    'arch_build2.c',
    'arch_cmplt.c',
    'arch_cmpltw.c',
    'arch_deco.c',
    'arch_deco2.c',
    'arch_dist.c',
    'arch_hcub.c',
    'arch_mesh.c',
    'arch_tleaf.c',
    'arch_sub.c',
    'arch_torus.c',
    'arch_vcmplt.c',
    'arch_vhcub.c',
    'bgraph.c',
    'bgraph_bipart_bd.c',
    'bgraph_bipart_df.c',
    'bgraph_bipart_ex.c',
    'bgraph_bipart_fm.c',
    'bgraph_bipart_ga.c',
    'bgraph_bipart_gg.c',
    'bgraph_bipart_gp.c',
    'bgraph_bipart_ml.c',
    'bgraph_bipart_st.c',
    'bgraph_bipart_zr.c',
    'bgraph_cost.c',
    'bgraph_check.c',
    'bgraph_cost.c',
    'bgraph_store.c',
    'common.c',
    'common_context.c',
    'common_error.c',
    'common_file.c',
    'common_file_compress.c',
    'common_file_decompress.c',
    'common_integer.c',
    'common_memory.c',
    'common_string.c',
    'common_stub.c',
    'common_thread.c',
    'common_thread_system.c',
    'common_timer.c',
    'common_values.c',
    'context.c',
    'fibo.c',
    'gain.c',
    'geom.c',
    'graph.c',
    'graph_band.c',
    'graph_base.c',
    'graph_check.c',
    'graph_clone.c',
    'graph_coarsen.c',
    'graph_diam.c',
    'graph_dump.c',
    'graph_ielo.c',
    'library_graph_induce.c',
    'graph_induce.c',
    'graph_io.c',
    'graph_io_chac.c',
    'graph_io_habo.c',
    'graph_io_mmkt.c',
    'graph_io_scot.c',
    'graph_list.c',
    'graph_match.c',
    'hall_order_hd.c',
    'hall_order_hf.c',
    'hall_order_hx.c',
    'hgraph.c',
    'hgraph_check.c',
    'hgraph_induce.c',
    'hgraph_order_bl.c',
    'hgraph_order_cc.c',
    'hgraph_order_cp.c',
    'hgraph_order_gp.c',
    'hgraph_order_hd.c',
    'hgraph_order_hf.c',
    'hgraph_order_hx.c',
    'hgraph_order_kp.c',
    'hgraph_order_nd.c',
    'hgraph_order_si.c',
    'hgraph_order_st.c',
    'hmesh.c',
    'hmesh_check.c',
    'hmesh_hgraph.c',
    'hmesh_induce.c',
    'hmesh_mesh.c',
    'hmesh_order_bl.c',
    'hmesh_order_cp.c',
    'hmesh_order_gp.c',
    'hmesh_order_gr.c',
    'hmesh_order_hd.c',
    'hmesh_order_hf.c',
    'hmesh_order_hx.c',
    'hmesh_order_nd.c',
    'hmesh_order_si.c',
    'hmesh_order_st.c',
    'kgraph.c',
    'kgraph_band.c',
    'kgraph_check.c',
    'kgraph_cost.c',
    'kgraph_map_bd.c',
    'kgraph_map_cp.c',
    'kgraph_map_df.c',
    'kgraph_map_ex.c',
    'kgraph_map_fm.c',
    'kgraph_map_ml.c',
    'kgraph_map_rb.c',
    'kgraph_map_rb_map.c',
    'kgraph_map_rb_part.c',
    'kgraph_map_st.c',
    'kgraph_store.c',
    'library_arch.c',
    'library_arch_build.c',
    'library_arch_build_f.c',
    'library_arch_dom.c',
    'library_arch_dom_f.c',
    'library_arch_f.c',
    'library_common.c',
    'library_common_f.c',
    'library_context.c',
    'library_context_graph.c',
    'library_context_graph_f.c',
    'library_context_f.c',
    'library_geom.c',
    'library_geom_f.c',
    'library_graph.c',
    'library_graph_base.c',
    'library_graph_base_f.c',
    'library_graph_check.c',
    'library_graph_check_f.c',
    'library_graph_coarsen.c',
    'library_graph_coarsen_f.c',
    'library_graph_color.c',
    'library_graph_color_f.c',
    'library_graph_diam.c',
    'library_graph_diam_f.c',
    'library_graph_dump.c',
    'library_graph_f.c',
    'library_graph_io_chac.c',
    'library_graph_io_chac_f.c',
    'library_graph_io_habo.c',
    'library_graph_io_habo_f.c',
    'library_graph_io_mmkt.c',
    'library_graph_io_mmkt_f.c',
    'library_graph_io_scot.c',
    'library_graph_io_scot_f.c',
    'library_graph_map.c',
    'library_graph_map_f.c',
    'library_graph_map_io.c',
    'library_graph_map_io_f.c',
    'library_graph_map_view.c',
    'library_graph_map_view_f.c',
    'library_graph_order.c',
    'library_graph_order_f.c',
    'library_graph_part_ovl.c',
    'library_graph_part_ovl_f.c',
    'library_mapping.c',
    'library_memory.c',
    'library_mesh.c',
    'library_mesh_f.c',
    'library_mesh_graph.c',
    'library_mesh_graph_f.c',
    'library_mesh_io_habo.c',
    'library_mesh_io_habo_f.c',
    'library_mesh_io_scot.c',
    'library_mesh_io_scot_f.c',
    'library_mesh_order.c',
    'library_mesh_order_f.c',
    'library_order.c',
    'library_parser.c',
    'library_parser_f.c',
    'library_random.c',
    'library_random_f.c',
    'library_strat.c',
    'library_version.c',
    'library_version_f.c',
    'mapping.c',
    'mapping_check.c',
    'mapping_io.c',
    'mesh.c',
    'mesh_check.c',
    'mesh_coarsen.c',
    'mesh_graph.c',
    'mesh_induce_sepa.c',
    'mesh_io.c',
    'mesh_io_habo.c',
    'mesh_io_scot.c',
    'order.c',
    'order_check.c',
    'order_io.c',
    'parser.c',
    'vgraph.c',
    'vgraph_check.c',
    'vgraph_separate_bd.c',
    'vgraph_separate_df.c',
    'vgraph_separate_es.c',
    'vgraph_separate_fm.c',
    'vgraph_separate_gg.c',
    'vgraph_separate_gp.c',
    'vgraph_separate_ml.c',
    'vgraph_separate_st.c',
    'vgraph_separate_th.c',
    'vgraph_separate_vw.c',
    'vgraph_separate_zr.c',
    'vgraph_store.c',
    'vmesh.c',
    'vmesh_check.c',
    'vmesh_separate_fm.c',
    'vmesh_separate_gg.c',
    'vmesh_separate_gr.c',
    'vmesh_separate_ml.c',
    'vmesh_separate_st.c',
    'vmesh_separate_zr.c',
    'vmesh_store.c',
    'wgraph.c',
    'wgraph_check.c',
    'wgraph_part_fm.c',
    'wgraph_part_es.c',
    'wgraph_part_ml.c',
    'wgraph_part_rb.c',
    'wgraph_part_st.c',
    'wgraph_part_zr.c',
    'wgraph_store.c',
  ),
  parser_yy_gen,
  parser_ll_gen,
  scotch_h_gen,
]

scotcherr_lib = library(
  'scotcherr',
  ['library_error.c', scotch_h_gen],
  c_args: c_args,
  include_directories: libscotch_inc,
  version: scotch_version_long,
  soversion: f'@scotch_version@.@scotch_release@',
)
scotcherr_dep = declare_dependency(
  link_with: scotcherr_lib,
  compile_args: c_args,
  include_directories: include_directories('.'),
  version: scotch_version_long,
)

scotcherrexit_lib = library(
  'scotcherrexit',
  ['library_error_exit.c', scotch_h_gen],
  c_args: c_args,
  include_directories: libscotch_inc,
  version: scotch_version_long,
  soversion: f'@scotch_version@.@scotch_release@',
)
scotcherrexit_dep = declare_dependency(
  link_with: scotcherrexit_lib,
  compile_args: c_args,
  include_directories: include_directories('.'),
  version: scotch_version_long,
)

scotch_args = c_args
scotch_deps = base_deps + [scotcherr_dep]

# Determinism
if scotch_deterministic == 'full'
  scotch_args += ['-DCOMMON_RANDOM_FIXED_SEED', '-DSCOTCH_DETERMINISTIC']
elif scotch_deterministic == 'fixed_seed'
  scotch_args += ['-DCOMMON_RANDOM_FIXED_SEED']
endif

if get_option('buildtype').startswith('debug')
  scotch_args += ['-DSCOTCH_DEBUG_ALL']
endif

zlib_dep  = dependency('zlib',  required: false)
if zlib_dep.found()
  scotch_args += ['-DCOMMON_FILE_COMPRESS_GZ']
  scotch_deps += [zlib_dep]
endif

bzip2_dep = dependency('bzip2', required: false)
if bzip2_dep.found()
  scotch_args += ['-DCOMMON_FILE_COMPRESS_BZ2']
  scotch_deps += [bzip2_dep]
endif

lzma_dep  = dependency('liblzma', required: false)
if lzma_dep.found()
  scotch_args += ['-DCOMMON_FILE_COMPRESS_LZMA']
  scotch_deps += [lzma_dep]
endif

if use_threads
  scotch_args += ['-DCOMMON_PTHREAD', '-DSCOTCH_PTHREAD']
  scotch_deps += [threads_dep]
endif

scotch_lib = library(
  'scotch',
  scotch_src,
  c_args: scotch_args,
  include_directories: libscotch_inc,
  dependencies: scotch_deps,
  version: scotch_version_long,
  soversion: f'@scotch_version@.@scotch_release@',
)
scotch_dep = declare_dependency(
  link_with: scotch_lib,
  compile_args: scotch_args,
  include_directories: include_directories('.'),
  dependencies: scotch_deps,
  version: scotch_version_long,
)

if build_ptscotch
  ptscotch_src = [
    files(
      'arch_mpi.c',
      'arch_cmplt_mpi.c',
      'arch_cmpltw_mpi.c',
      'arch_deco_mpi.c',
      'arch_deco2_mpi.c',
      'arch_dist_mpi.c',
      'arch_hcub_mpi.c',
      'arch_mesh_mpi.c',
      'arch_sub_mpi.c',
      'arch_tleaf_mpi.c',
      'arch_vcmplt_mpi.c',
      'arch_vhcub_mpi.c',
      'bdgraph.c',
      'bdgraph_bipart_bd.c',
      'bdgraph_bipart_df.c',
      'bdgraph_bipart_ex.c',
      'bdgraph_bipart_ml.c',
      'bdgraph_bipart_sq.c',
      'bdgraph_bipart_st.c',
      'bdgraph_bipart_zr.c',
      'bdgraph_check.c',
      'bdgraph_gather_all.c',
      'bdgraph_store.c',
      'comm.c',
      'dgraph.c',
      'dgraph_allreduce.c',
      'dgraph_band.c',
      'dgraph_build.c',
      'dgraph_build_grid3d.c',
      'dgraph_build_hcub.c',
      'dgraph_check.c',
      'dgraph_coarsen.c',
      'dgraph_compact.c',
      'dgraph_fold.c',
      'dgraph_fold_comm.c',
      'dgraph_fold_dup.c',
      'dgraph_gather.c',
      'dgraph_gather_all.c',
      'dgraph_ghst.c',
      'dgraph_halo.c',
      'dgraph_induce.c',
      'dgraph_io_load.c',
      'dgraph_io_save.c',
      'dgraph_match.c',
      'dgraph_match_check.c',
      'dgraph_match_sync_coll.c',
      'dgraph_match_sync_ptop.c',
      'dgraph_redist.c',
      'dgraph_scatter.c',
      'dgraph_view.c',
      'dmapping.c',
      'dmapping_io.c',
      'dmesh.c',
      'dmesh_build_adm.c',
      'dmesh_dgraph.c',
      'dmesh_io_load.c',
      'dorder.c',
      'dorder_gather.c',
      'dorder_io.c',
      'dorder_io_block.c',
      'dorder_io_tree.c',
      'dorder_perm.c',
      'dorder_tree_dist.c',
      'hdgraph.c',
      'hdgraph_check.c',
      'hdgraph_fold.c',
      'hdgraph_gather.c',
      'hdgraph_induce.c',
      'hdgraph_order_nd.c',
      'hdgraph_order_si.c',
      'hdgraph_order_sq.c',
      'hdgraph_order_st.c',
      'kdgraph.c',
      'kdgraph_gather.c',
      'kdgraph_map_rb.c',
      'kdgraph_map_rb_map.c',
      'kdgraph_map_rb_part.c',
      'kdgraph_map_st.c',
      'library_context_dgraph.c',
      'library_context_dgraph_f.c',
      'library_dgraph.c',
      'library_dgraph_band.c',
      'library_dgraph_band_f.c',
      'library_dgraph_build.c',
      'library_dgraph_build_f.c',
      'library_dgraph_build_grid3d.c',
      'library_dgraph_build_grid3d_f.c',
      'library_dgraph_check.c',
      'library_dgraph_check_f.c',
      'library_dgraph_coarsen.c',
      'library_dgraph_coarsen_f.c',
      'library_dgraph_f.c',
      'library_dgraph_gather.c',
      'library_dgraph_gather_f.c',
      'library_dgraph_grow.c',
      'library_dgraph_halo.c',
      'library_dgraph_halo_f.c',
      'library_dgraph_induce.c',
      'library_dgraph_induce_f.c',
      'library_dgraph_io_load.c',
      'library_dgraph_io_load_f.c',
      'library_dgraph_io_save.c',
      'library_dgraph_io_save_f.c',
      'library_dgraph_map.c',
      'library_dgraph_map_f.c',
      'library_dgraph_map_stat.c',
      'library_dgraph_map_stat_f.c',
      'library_dgraph_map_view.c',
      'library_dgraph_map_view_f.c',
      'library_dgraph_order.c',
      'library_dgraph_order_f.c',
      'library_dgraph_order_gather.c',
      'library_dgraph_order_gather_f.c',
      'library_dgraph_order_io.c',
      'library_dgraph_order_io_block.c',
      'library_dgraph_order_io_block_f.c',
      'library_dgraph_order_io_f.c',
      'library_dgraph_order_perm.c',
      'library_dgraph_order_perm_f.c',
      'library_dgraph_order_tree_dist.c',
      'library_dgraph_order_tree_dist_f.c',
      'library_dgraph_redist.c',
      'library_dgraph_redist_f.c',
      'library_dgraph_scatter.c',
      'library_dgraph_scatter_f.c',
      'library_dgraph_stat.c',
      'library_dgraph_stat_f.c',
      'library_dmapping.c',
      'library_dmesh.c',
      'library_dmesh_f.c',
      'library_dmesh_build_adm.c',
      'library_dmesh_build_adm_f.c',
      'library_dmesh_dgraph.c',
      'library_dmesh_dgraph_f.c',
      'library_dmesh_io_load.c',
      'library_dmesh_io_load_f.c',
      'library_dorder.c',
      'vdgraph.c',
      'vdgraph_check.c',
      'vdgraph_gather_all.c',
      'vdgraph_separate_bd.c',
      'vdgraph_separate_df.c',
      'vdgraph_separate_ml.c',
      'vdgraph_separate_sq.c',
      'vdgraph_separate_st.c',
      'vdgraph_separate_zr.c',
      'vdgraph_store.c',
    ),
    scotch_h_gen,
    ptscotch_h_gen,
  ]

  ptscotcherr_lib = library(
    'ptscotcherr',
    ['library_error.c', scotch_h_gen, ptscotch_h_gen],
    c_args: c_args,
    include_directories: libscotch_inc,
    version: scotch_version_long,
    soversion: f'@scotch_version@.@scotch_release@',
  )
  ptscotcherr_dep = declare_dependency(
    link_with: ptscotcherr_lib,
    compile_args: c_args,
    include_directories: include_directories('.'),
    version: scotch_version_long,
  )

  ptscotcherrexit_lib = library(
    'ptscotcherrexit',
    ['library_error_exit.c', scotch_h_gen, ptscotch_h_gen],
    c_args: c_args,
    include_directories: libscotch_inc,
    version: scotch_version_long,
    soversion: f'@scotch_version@.@scotch_release@',
  )
  ptscotcherrexit_dep = declare_dependency(
    link_with: ptscotcherrexit_lib,
    compile_args: c_args,
    include_directories: include_directories('.'),
    version: scotch_version_long,
  )

  ptscotch_deps = [mpi_dep, scotch_dep, ptscotcherr_dep]
  ptscotch_args = c_args + ['-DSCOTCH_PTSCOTCH']

  if has_mpi_multithread
    ptscotch_deps += [threads_dep]
    ptscotch_args += ['-DSCOTCH_PTHREAD', '-DCOMMON_PTHREAD']
  endif

  ptscotch_lib = library(
    'ptscotch',
    ptscotch_src,
    c_args: ptscotch_args,
    include_directories: libscotch_inc,
    dependencies: ptscotch_deps,
    version: scotch_version_long,
    soversion: f'@scotch_version@.@scotch_release@',
  )
  ptscotch_dep = declare_dependency(
    link_with: ptscotch_lib,
    compile_args: ptscotch_args,
    include_directories: include_directories('.'),
    dependencies: ptscotch_deps,
    version: scotch_version_long,
  )
endif

# TODO Installing
