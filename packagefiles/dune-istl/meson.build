# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'dune-istl',
  'c',
  'cpp',
  version: '2.11.0',
  default_options: ['cpp_std=c++20', 'warning_level=3'],
)

mod_version = '2.11.0'
mod_version_split = mod_version.split('.')

cpp_compiler = meson.get_compiler('cpp')

args = []
deps = []

with_metis = get_option('with_metis')
with_scotch = get_option('with_scotch')
with_parmetis = get_option('with_parmetis')
with_ptscotch = get_option('with_ptscotch')
dune_common_sub = subproject(
  'dune-common',
  default_options: [
    f'with_metis=@with_metis@',
    f'with_scotch=@with_scotch@',
    f'with_parmetis=@with_parmetis@',
    f'with_ptscotch=@with_ptscotch@',
  ],
)
dune_common_dep = dune_common_sub.get_variable('dune_common_dep')
deps += [dune_common_dep]

# Read module file
fs = import('fs')
mod_info = {}
foreach l : fs.read('dune.module').strip().split('\n')
  if l == ''
    continue
  endif

  split = l.split(':')
  key = split[0]
  value = split[1]
  foreach i : range(2, split.length())
    value += ':' + split[i]
  endforeach
  value = value.strip()
  mod_info += {key: value}
endforeach

python3_prg = find_program('python3')

cfg = {
  'DUNE_MAINTAINER': mod_info['Maintainer'],
  'DUNE_MOD_NAME': mod_info['Module'],
  'DUNE_MOD_URL': mod_info['URL'],
  'DUNE_MOD_VERSION': mod_version,
  'DUNE_ISTL_VERSION': mod_version,
  'DUNE_ISTL_VERSION_MAJOR': mod_version_split[0].to_int(),
  'DUNE_ISTL_VERSION_MINOR': mod_version_split[1].to_int(),
  'DUNE_ISTL_VERSION_REVISION': mod_version_split[2].to_int(),
}

superlu_dep = dependency('superlu', required: false)
if superlu_dep.found()
  if superlu_dep.type_name() == 'internal'
    superlu_int = subproject('superlu').get_variable('int_t')
  else
    test_res = cpp_compiler.run(
      '''
      #include <cstdio>
      #include <type_traits>
      #include <slu_sdefs.h>
      int main() {
        if constexpr (std::is_same_v<int_t, int>) std::puts("int");
        else if constexpr (std::is_same_v<int_t, long>) std::puts("long");
        else return 1;
      }
      ''',
      dependencies: [superlu_dep],
    )
    assert(test_res.compiled() and test_res.returncode() == 0)
    superlu_int = test_res.stdout().strip()
  endif
  deps += [superlu_dep]
  cfg += {'SUPERLU_INT_TYPE': superlu_int}
  args += ['-DHAVE_SUPERLU=1']
endif

arpackpp_dep = subproject('arpackpp').get_variable('arpackpp_dep')
deps += [arpackpp_dep]
args += ['-DHAVE_ARPACKPP=1']

config_file_py = dune_common_sub.get_variable('config_file_py')
dune_common_config_h = dune_common_sub.get_variable('config_h')
config_str = ''
foreach key, value : cfg
  config_str += f'@key@=@value@\n'
endforeach
config_h = configure_file(
  input: 'config.h.cmake',
  output: 'dune-istl-config.hh',
  command: [
    python3_prg,
    config_file_py,
    dune_common_config_h,
    '@INPUT@',
    '@OUTPUT@',
    config_str,
  ],
)

dune_istl_dep = declare_dependency(
  compile_args: args,
  dependencies: deps,
  include_directories: include_directories('.'),
)

if get_option('test')
  subdir('dune/istl')
endif
