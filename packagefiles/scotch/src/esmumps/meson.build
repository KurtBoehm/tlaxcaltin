esmumps_h = configure_file(
  input: 'library.h',
  output: 'esmumps.h',
  copy: true,
)

######################
# libEsMUMPS sources #
######################

esmumps_src = files(
  'dof.c',
  'esmumps.c',
  'graph_graph.c',
  'library_esmumps.c',
  'library_esmumps_f.c',
  'library_esmumps_strats.c',
  'order.c',
  'order_check.c',
  'order_io.c',
  'order_scotch_graph.c',
  'symbol.c',
  'symbol_check.c',
  'symbol_cost.c',
  'symbol_fax.c',
  'symbol_fax_graph.c',
)

esmumps_headers = files(
  'dof.h',
  'fax.h',
  'graph.h',
  'library.h',
  'module.h',
  'order.h',
  'symbol.h',
)

###################
# esmumps library #
###################

is_darwin = host_machine.system() == 'darwin'

esmumps_link_args = []
if is_darwin
  esmumps_link_args += ['-undefined', 'dynamic_lookup']
endif

esmumps_lib = library(
  'esmumps',
  sources: [esmumps_src, esmumps_headers, esmumps_h, scotch_h],
  include_directories: [libscotch_inc],
  dependencies: [scotch_dep],
  version: scotch_version_long,
  soversion: f'@scotch_version@.@scotch_release@',
  link_args: esmumps_link_args,
)
esmumps_dep = declare_dependency(
  link_with: esmumps_lib,
  include_directories: [libscotch_inc],
  sources: [scotch_h],
)
meson.override_dependency('esmumps', esmumps_dep)

#####################
# ptesmumps library #
#####################

if build_ptscotch
  ptesmumps_lib = library(
    'ptesmumps',
    sources: [esmumps_src, esmumps_headers, esmumps_h, scotch_h],
    include_directories: [libscotch_inc],
    dependencies: [ptscotch_dep],
    version: scotch_version_long,
    soversion: f'@scotch_version@.@scotch_release@',
    link_args: esmumps_link_args,
  )
  ptesmumps_dep = declare_dependency(
    link_with: ptesmumps_lib,
    include_directories: [libscotch_inc],
    sources: [scotch_h],
  )
  meson.override_dependency('ptesmumps', ptesmumps_dep)
endif
