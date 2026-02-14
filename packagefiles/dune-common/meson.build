# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'dune-common',
  'c',
  'cpp',
  version: '2.11.0',
  default_options: ['cpp_std=c++20', 'warning_level=3'],
)

mod_version = '2.11.0'
mod_version_split = mod_version.split('.')
mod_version_major = mod_version_split[0].to_int()
mod_version_minor = mod_version_split[1].to_int()
mod_version_rev = mod_version_split[2].to_int()

cpp_compiler = meson.get_compiler('cpp')
has_id_detected = cpp_compiler.compiles(
  '''
  #include <experimental/type_traits>
  static_assert(__cpp_lib_experimental_detect >= 201505);
  int main() {}
  ''',
)
message(f'Has is_detected and friends: @has_id_detected@')

has_unevaluated_lambda = cpp_compiler.compiles(
  'using lambda = decltype([](){}); int main() {}',
)
message(f'Supports lambdas in unevaluated contexts: @has_unevaluated_lambda@')

has_identity = cpp_compiler.compiles(
  '''
  #include <functional>
  int main() {
    return std::identity{}(0);
  }
  ''',
)
message(f'Has std::identity: @has_identity@')

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

args = []
deps = []
cfg = {
  'DUNE_COMMON_VERSION': f'@mod_version_major@.@mod_version_minor@',
  'DUNE_COMMON_VERSION_MAJOR': mod_version_major,
  'DUNE_COMMON_VERSION_MINOR': mod_version_minor,
  'DUNE_COMMON_VERSION_REVISION': mod_version_rev,
  'DUNE_MINIMAL_DEBUG_LEVEL': 4,
  # TODO DUNE_HAVE_CXX_EXPERIMENTAL_MAKE_ARRAY is deprecated anyway
  'DUNE_HAVE_CXX_EXPERIMENTAL_IS_DETECTED': has_id_detected.to_int(),
  'DUNE_HAVE_CXX_UNEVALUATED_CONTEXT_LAMBDA': has_unevaluated_lambda.to_int(),
  'DUNE_HAVE_CXX_STD_IDENTITY': has_identity.to_int(),
  'DUNE_MAINTAINER': mod_info['Maintainer'],
  'DUNE_MOD_NAME': mod_info['Module'],
  'DUNE_MOD_URL': mod_info['URL'],
  'DUNE_MOD_VERSION': mod_version,
}

blas_dep = dependency('blas', required: false)
if blas_dep.found()
  deps += [blas_dep]
  cfg += {'HAVE_BLAS': 1}
endif
lapack_dep = dependency('lapack', required: false)
if lapack_dep.found()
  deps += [lapack_dep]
  cfg += {'HAVE_LAPACK': 1}

  if lapack_dep.type_name() == 'internal'
    needs_underline = true
  else
    needs_underline = cpp_compiler.compiles(
      '''
      #include <cstdint>
      extern "C" {
      extern void dsyev_(const char* jobz, const char* uplo, const long int* n, double* a,
                        const long int* lda, double* w, double* work, const long int* lwork,
                        long int* info);
      }
      int main() { uintptr_t v = (uintptr_t)dsyev_; }
      ''',
      dependencies: [lapack_dep],
    )
  endif
  message(f'LAPACK needs underline: @needs_underline@')

  if needs_underline
    cfg += {'LAPACK_NEEDS_UNDERLINE': 1}
  endif
endif
mpi_sub = subproject('mpi-c', required: false)
if mpi_sub.found()
  deps += [mpi_sub.get_variable('mpi_dep')]
  args += ['-DHAVE_MPI=1']
endif
gmp_dep = dependency('gmpxx', required: false)
if gmp_dep.found()
  deps += [gmp_dep]
  args += ['-DHAVE_GMP=1']
endif
quadmath_dep = cpp_compiler.find_library('quadmath', required: false)
quadmath_args = []
if cpp_compiler.get_id() == 'gcc'
  quadmath_args += ['-fext-numeric-literals']
endif
has_quadmath = cpp_compiler.compiles(
  '''
  #include <quadmath.h>
  int main() {
    __float128 r = 1.0q;
    r = strtoflt128("1.2345678", nullptr);
  }
  ''',
  args: quadmath_args,
  dependencies: quadmath_dep,
)
if has_quadmath
  deps += [quadmath_dep]
  args += quadmath_args + ['-DHAVE_QUADMATH=1']
endif
vc_dep = dependency('Vc', required: false)
if vc_dep.found()
  deps += [vc_dep]
  args += ['-DHAVE_VC=1']
endif
# TBB is not used

suitesparse = subproject('suitesparse')
deps += [
  suitesparse.get_variable('amd_dep'),
  suitesparse.get_variable('btf_dep'),
  suitesparse.get_variable('camd_dep'),
  suitesparse.get_variable('ccolamd_dep'),
  suitesparse.get_variable('colamd_dep'),
  suitesparse.get_variable('cholmod_dep'),
  suitesparse.get_variable('cxsparse_dep'),
  suitesparse.get_variable('klu_dep'),
  suitesparse.get_variable('ldl_dep'),
  suitesparse.get_variable('umfpack_dep'),
  suitesparse.get_variable('rbio_dep'),
  suitesparse.get_variable('spqr_dep'),
]
args += [
  '-DHAVE_SUITESPARSE_CHOLMOD=1',
  '-DHAVE_SUITESPARSE_LDL=1',
  '-DHAVE_SUITESPARSE_SPQR=1',
  '-DHAVE_SUITESPARSE_UMFPACK=1',
]

with_metis = get_option('with_metis')
with_scotch = get_option('with_scotch')
with_parmetis = get_option('with_parmetis')
with_ptscotch = get_option('with_ptscotch')
assert(
  not with_metis or not with_scotch,
  'At most one sequential graph partioner can be added!',
)
assert(
  not with_parmetis or not with_ptscotch,
  'At most one parallel graph partioner can be added!',
)

if with_metis
  metis_dep = subproject('metis').get_variable('metis_dep')
  args += ['-DMETIS_API_VERSION=5', '-DHAVE_METIS=1']
  deps += [metis_dep]
endif

if with_parmetis
  parmetis_dep = subproject('parmetis').get_variable('parmetis_dep')
  args += ['-DHAVE_PARMETIS=1']
  deps += [parmetis_dep]
endif

if with_scotch or with_ptscotch
  scotch_sub = subproject('scotch')
  if with_scotch
    scotchmetis5_dep = scotch_sub.get_variable('scotchmetis5_dep')
    args += ['-DMETIS_API_VERSION=5', '-DHAVE_SCOTCH_METIS=1', '-DHAVE_METIS=1']
    deps += [scotchmetis5_dep]
  endif
  if with_ptscotch
    ptscotchparmetis3_dep = scotch_sub.get_variable('ptscotchparmetis3_dep')
    args += ['-DHAVE_PTSCOTCH=1', '-DHAVE_PTSCOTCH_PARMETIS=1', '-DHAVE_PARMETIS=1']
    deps += [ptscotchparmetis3_dep]
  endif
endif

config_file_py = files('meson_python/configure_file.py')
config_str = ''
foreach key, value : cfg
  config_str += f'@key@=@value@\n'
endforeach
config_h = configure_file(
  input: 'config.h.cmake',
  output: 'dune-common-config.hh',
  command: [python3_prg, config_file_py, '@INPUT@', '@OUTPUT@', config_str],
)
dune_common_inc = include_directories('.')
args += ['-DHAVE_CONFIG_H=1']

dune_common_src = [
  'dune/common/debugalign.cc',
  'dune/common/debugallocator.cc',
  'dune/common/exceptions.cc',
  'dune/common/fmatrixev.cc',
  'dune/common/ios_state.cc',
  'dune/common/parametertree.cc',
  'dune/common/parametertreeparser.cc',
  'dune/common/path.cc',
  'dune/common/simd/test.cc',
  'dune/common/stdstreams.cc',
  'dune/common/stdthread.cc',
]

dune_common_lib = shared_library(
  'dune_common',
  dune_common_src,
  cpp_args: args,
  dependencies: deps,
  include_directories: [dune_common_inc],
)
dune_common_dep = declare_dependency(
  link_with: dune_common_lib,
  compile_args: args,
  dependencies: deps,
  include_directories: [dune_common_inc],
)

if get_option('test')
  subdir('dune/common/test')
endif
