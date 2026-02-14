# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

metis_h_gen = custom_target(
  'dummysizes_metis_h',
  input: ['library_metis.h'],
  output: ['metis.h'],
  command: [dummysizes_exe, '@INPUT@', '@OUTPUT@'],
  install: true,
  install_dir: get_option('includedir'),
)
metisf_h_gen = custom_target(
  'dummysizes_metisf_h',
  input: ['library_metis_f.h'],
  output: ['metisf.h'],
  command: [dummysizes_exe, '@INPUT@', '@OUTPUT@'],
  install: true,
  install_dir: get_option('includedir'),
)

scotchmetis_deps = []
foreach version : [3, 5]
  # TODO Fortran
  scotchmetis_sources = [
    'metis_graph_order.c',
    'metis_graph_part.c',
    'metis_graph_dual.c',
    'metis_graph_part_dual.c',
    'metis_options.c',
    metis_h_gen,
  ]

  deps = base_deps + [scotch_dep]
  args = c_args + [f'-DSCOTCH_METIS_VERSION=@version@']

  scotchmetis_lib = shared_library(
    f'scotchmetis@version@',
    scotchmetis_sources,
    c_args: args,
    include_directories: [include_directories('.')],
    dependencies: deps,
    version: scotch_version_long,
  )
  scotchmetis_deps += [
    declare_dependency(
      link_with: scotchmetis_lib,
      sources: [metis_h_gen],
      compile_args: args,
      dependencies: deps,
      include_directories: include_directories('.'),
    ),
  ]
endforeach
scotchmetis3_dep = scotchmetis_deps[0]
scotchmetis5_dep = scotchmetis_deps[1]

if build_ptscotch
  parmetis_h_gen = custom_target(
    'dummysizes_parmetis_h',
    input: ['library_parmetis.h'],
    output: ['parmetis.h'],
    command: [dummysizes_exe, '@INPUT@', '@OUTPUT@'],
    install: true,
    install_dir: get_option('includedir'),
  )

  # TODO Fortran
  ptscotchparmetis_sources = [
    'parmetis_dgraph_order.c',
    'parmetis_dgraph_part.c',
    parmetis_h_gen,
  ]

  ptscotchparmetis_deps = []
  foreach version : [3]
    deps = base_deps + [mpi_dep, ptscotch_dep]
    args = c_args + ['-DSCOTCH_PTSCOTCH', f'-DSCOTCH_PARMETIS_VERSION=@version@']

    ptscotchparmetis_lib = shared_library(
      f'ptscotchparmetis@version@',
      ptscotchparmetis_sources,
      c_args: args,
      include_directories: [include_directories('.')],
      dependencies: deps,
      version: scotch_version_long,
    )
    ptscotchparmetis_deps += [
      declare_dependency(
        link_with: ptscotchparmetis_lib,
        sources: [parmetis_h_gen],
        compile_args: args,
        dependencies: deps,
        include_directories: include_directories('.'),
      ),
    ]
  endforeach
  ptscotchparmetis3_dep = ptscotchparmetis_deps[0]
endif

# TODO Installing
