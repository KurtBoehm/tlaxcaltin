# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

flex_prg = find_program('flex', required: false)
bison_prg = find_program('bison', required: false)

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

threads_dep = dependency('threads', required: false)
mpi_dep = subproject('mpi-c').get_variable('mpi_dep')

c_args += [
  '-Drestrict=__restrict',
  '-DCOMMON_RANDOM_FIXED_SEED',
  '-DSCOTCH_RENAME',
]
os = build_machine.system()
if os == 'darwin'
  c_args += ['-DCOMMON_OS_MACOS', '-D_DARWIN_C_SOURCE']
endif
if os == 'windows'
  c_args += ['-DCOMMON_OS_WINDOWS']
endif

int_size = get_option('int_size')
if int_size == 32
  c_args += ['-DINTSIZE32']
elif int_size == 64
  c_args += ['-DINTSIZE64']
elif int_size != 0
  error(f'Invalid integer size @int_size@')
endif

use_threads = get_option('threads')
if use_threads
  assert(
    threads_dep.found(),
    'Threads were requested, but have not been found!',
  )
  c_args += ['-DCOMMON_PTHREAD', '-DSCOTCH_PTHREAD']

  # TODO _GNU_SOURCE
  affinity_prefix = '''
    #define _GNU_SOURCE
    #include <pthread.h>
  '''
  if cc.has_function('pthread_setaffinity_np', prefix: affinity_prefix)
    c_args += ['-DCOMMON_PTHREAD_AFFINITY_LINUX']
  endif
endif

build_ptscotch = get_option('build_ptscotch')
force_mpi_multithread = get_option('force_mpi_multithread')
if build_ptscotch
  assert(mpi_dep.found(), 'PT-Scotch cannot be built without MPI!')
  # TODO No oversubscribe check
  if threads_dep.found()
    if force_mpi_multithread
      assert(threads_dep.found(), 'Threads are required for multithreaded MPI!')
    endif
    test_program = '''
      #include <stdio.h>
      #include <stdlib.h>
      #include <mpi.h>

      int main(int argc, char** argv) {
        int prov;
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &prov);
        MPI_Finalize();
        return (prov < MPI_THREAD_MULTIPLE) ? EXIT_FAILURE : EXIT_SUCCESS;
      }
    '''
    has_mpi_multithread = (
      cc.run(test_program, dependencies: [mpi_dep, threads_dep]).returncode() == 0
    )
    if force_mpi_multithread
      assert(has_mpi_multithread, 'Multithreaded MPI does not seem to work!')
    endif
    if has_mpi_multithread
      c_args += ['-DSCOTCH_PTHREAD_MPI']
    endif
  endif
endif

# Build Scotch and PT-Scotch libraries
subdir('libscotch')

# Build Scotch executables
# TODO subdir('scotch')

# Build EsMUMPS library
if get_option('build_libesmumps')
  # TODO subdir('esmumps')
endif

# Build ScotchMeTiS library
if get_option('build_libscotchmetis')
  subdir('libscotchmetis')
endif

# Testing
# TODO subdir('check')
