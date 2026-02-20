# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

examples_deps = [ginkgo_dep]

subdir('adaptiveprecision-blockjacobi')
subdir('batched-solver')
subdir('cb-gmres')
subdir('custom-logger')
subdir('ginkgo-ranges')
subdir('ilu-preconditioned-solver')
subdir('ir-ilu-preconditioned-solver')
subdir('inverse-iteration')
subdir('iterative-refinement')
subdir('mixed-precision-ir')
subdir('nine-pt-stencil-solver')
subdir('poisson-solver')
subdir('preconditioned-solver')
subdir('simple-solver')
subdir('three-pt-stencil-solver')
subdir('custom-stopping-criterion')
subdir('file-config-solver')
subdir('ginkgo-overhead')
subdir('minimal-cuda-solver')
subdir('mixed-spmv')
subdir('mixed-multigrid-preconditioned-solver')
subdir('mixed-multigrid-solver')
subdir('multigrid-preconditioned-solver')
subdir('multigrid-preconditioned-solver-customized')
subdir('par-ilu-convergence')
subdir('performance-debugging')
subdir('preconditioner-export')
subdir('reordered-preconditioned-solver')
subdir('simple-solver-logging')
subdir('distributed-solver')
# subdir('kokkos-assembly/kokkos-assembly.cpp')

ocv = dependency('opencv4', required: false)
if ocv.found()
  examples_deps += [ocv]
  subdir('heat-equation')
  subdir('schroedinger-splitting')
endif
