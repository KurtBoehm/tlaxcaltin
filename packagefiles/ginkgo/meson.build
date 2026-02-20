# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

project(
  'ginkgo',
  'cpp',
  'c',
  version: '1.11.0',
)

hwloc_dep = dependency('hwloc', required: false)
metis_dep = dependency('metis')
omp_dep = dependency('OpenMP')

with_mpi = get_option('mpi_implementation') != 'none'
if with_mpi
  mpi_sub = subproject('mpi-c')
  mpi_dep = mpi_sub.get_variable('mpi_dep')
  mpirun = mpi_sub.get_variable('mpirun')
else
  mpi_dep = []
endif

code = '''
#include <type_traits>
#include <cstddef>
#include <cstdint>
static_assert(std::is_same<std::uint64_t, std::size_t>::value);
int main() {}
'''
gko_size_t_is_uint64_t = meson.get_compiler('cpp').compiles(code)

cfg = {
  'Ginkgo_VERSION_MAJOR': 1,
  'Ginkgo_VERSION_MINOR': 11,
  'Ginkgo_VERSION_PATCH': 0,
  'Ginkgo_VERSION_TAG': 'main',
  'GINKGO_VERSION_TAG_DEPRECATED': 0,
  'GKO_VERSION_STR': '1, 11, 0',
  'GINKGO_VERBOSE_LEVEL': 1,
  'GKO_HAVE_CXXABI_H': true,
  'GKO_SIZE_T_IS_UINT64_T': gko_size_t_is_uint64_t,
  'GINKGO_MIXED_PRECISION': true,
  'GINKGO_DPCPP_MAJOR_VERSION': 0,
  'GINKGO_DPCPP_MINOR_VERSION': 0,
  'GINKGO_HAVE_PAPI_SDE': false,
  'GINKGO_HAVE_TAU': false,
  'GINKGO_HAVE_VTUNE': false,
  'GINKGO_HAVE_METIS': true,
  # TODO Make generic?
  'METIS_HEADER': 'metis.h',
  'GINKGO_HAVE_ROCTX': false,
  'GINKGO_BUILD_MPI': with_mpi,
  'GINKGO_HAVE_HWLOC': hwloc_dep.found(),
  'GINKGO_ENABLE_HALF': true,
}
gko_public_header_contents = '''
#include <ginkgo/core/base/abstract_factory.hpp>
#include <ginkgo/core/base/array.hpp>
#include <ginkgo/core/base/batch_dim.hpp>
#include <ginkgo/core/base/batch_lin_op.hpp>
#include <ginkgo/core/base/batch_multi_vector.hpp>
#include <ginkgo/core/base/bfloat16.hpp>
#include <ginkgo/core/base/block_operator.hpp>
#include <ginkgo/core/base/combination.hpp>
#include <ginkgo/core/base/composition.hpp>
#include <ginkgo/core/base/dense_cache.hpp>
#include <ginkgo/core/base/device.hpp>
#include <ginkgo/core/base/device_matrix_data.hpp>
#include <ginkgo/core/base/dim.hpp>
#include <ginkgo/core/base/event.hpp>
#include <ginkgo/core/base/exception_helpers.hpp>
#include <ginkgo/core/base/exception.hpp>
#include <ginkgo/core/base/executor.hpp>
#include <ginkgo/core/base/fwd_decls.hpp>
#include <ginkgo/core/base/half.hpp>
#include <ginkgo/core/base/index_set.hpp>
#include <ginkgo/core/base/intrinsics.hpp>
#include <ginkgo/core/base/lin_op.hpp>
#include <ginkgo/core/base/machine_topology.hpp>
#include <ginkgo/core/base/math.hpp>
#include <ginkgo/core/base/matrix_assembly_data.hpp>
#include <ginkgo/core/base/matrix_data.hpp>
#include <ginkgo/core/base/memory.hpp>
#include <ginkgo/core/base/mpi.hpp>
#include <ginkgo/core/base/mtx_io.hpp>
#include <ginkgo/core/base/name_demangling.hpp>
#include <ginkgo/core/base/perturbation.hpp>
#include <ginkgo/core/base/polymorphic_object.hpp>
#include <ginkgo/core/base/precision_dispatch.hpp>
#include <ginkgo/core/base/range_accessors.hpp>
#include <ginkgo/core/base/range.hpp>
#include <ginkgo/core/base/scoped_device_id_guard.hpp>
#include <ginkgo/core/base/segmented_array.hpp>
#include <ginkgo/core/base/std_extensions.hpp>
#include <ginkgo/core/base/stream.hpp>
#include <ginkgo/core/base/temporary_clone.hpp>
#include <ginkgo/core/base/temporary_conversion.hpp>
#include <ginkgo/core/base/timer.hpp>
#include <ginkgo/core/base/types.hpp>
#include <ginkgo/core/base/type_traits.hpp>
#include <ginkgo/core/base/utils_helper.hpp>
#include <ginkgo/core/base/version.hpp>
#include <ginkgo/core/config/config.hpp>
#include <ginkgo/core/config/property_tree.hpp>
#include <ginkgo/core/config/registry.hpp>
#include <ginkgo/core/config/type_descriptor.hpp>
#include <ginkgo/core/distributed/assembly.hpp>
#include <ginkgo/core/distributed/base.hpp>
#include <ginkgo/core/distributed/collective_communicator.hpp>
#include <ginkgo/core/distributed/dense_communicator.hpp>
#include <ginkgo/core/distributed/index_map.hpp>
#include <ginkgo/core/distributed/matrix.hpp>
#include <ginkgo/core/distributed/neighborhood_communicator.hpp>
#include <ginkgo/core/distributed/partition_helpers.hpp>
#include <ginkgo/core/distributed/partition.hpp>
#include <ginkgo/core/distributed/preconditioner/schwarz.hpp>
#include <ginkgo/core/distributed/row_gatherer.hpp>
#include <ginkgo/core/distributed/vector_cache.hpp>
#include <ginkgo/core/distributed/vector.hpp>
#include <ginkgo/core/factorization/cholesky.hpp>
#include <ginkgo/core/factorization/factorization.hpp>
#include <ginkgo/core/factorization/ic.hpp>
#include <ginkgo/core/factorization/ilu.hpp>
#include <ginkgo/core/factorization/incomplete_factorization.hpp>
#include <ginkgo/core/factorization/lu.hpp>
#include <ginkgo/core/factorization/par_ic.hpp>
#include <ginkgo/core/factorization/par_ict.hpp>
#include <ginkgo/core/factorization/par_ilu.hpp>
#include <ginkgo/core/factorization/par_ilut.hpp>
#include <ginkgo/core/log/batch_logger.hpp>
#include <ginkgo/core/log/convergence.hpp>
#include <ginkgo/core/log/logger.hpp>
#include <ginkgo/core/log/papi.hpp>
#include <ginkgo/core/log/performance_hint.hpp>
#include <ginkgo/core/log/profiler_hook.hpp>
#include <ginkgo/core/log/record.hpp>
#include <ginkgo/core/log/solver_progress.hpp>
#include <ginkgo/core/log/stream.hpp>
#include <ginkgo/core/matrix/batch_csr.hpp>
#include <ginkgo/core/matrix/batch_dense.hpp>
#include <ginkgo/core/matrix/batch_ell.hpp>
#include <ginkgo/core/matrix/batch_identity.hpp>
#include <ginkgo/core/matrix/coo.hpp>
#include <ginkgo/core/matrix/csr.hpp>
#include <ginkgo/core/matrix/dense.hpp>
#include <ginkgo/core/matrix/diagonal.hpp>
#include <ginkgo/core/matrix/ell.hpp>
#include <ginkgo/core/matrix/fbcsr.hpp>
#include <ginkgo/core/matrix/fft.hpp>
#include <ginkgo/core/matrix/hybrid.hpp>
#include <ginkgo/core/matrix/identity.hpp>
#include <ginkgo/core/matrix/permutation.hpp>
#include <ginkgo/core/matrix/row_gatherer.hpp>
#include <ginkgo/core/matrix/scaled_permutation.hpp>
#include <ginkgo/core/matrix/sellp.hpp>
#include <ginkgo/core/matrix/sparsity_csr.hpp>
#include <ginkgo/core/multigrid/fixed_coarsening.hpp>
#include <ginkgo/core/multigrid/multigrid_level.hpp>
#include <ginkgo/core/multigrid/pgm.hpp>
#include <ginkgo/core/preconditioner/batch_jacobi.hpp>
#include <ginkgo/core/preconditioner/gauss_seidel.hpp>
#include <ginkgo/core/preconditioner/ic.hpp>
#include <ginkgo/core/preconditioner/ilu.hpp>
#include <ginkgo/core/preconditioner/isai.hpp>
#include <ginkgo/core/preconditioner/jacobi.hpp>
#include <ginkgo/core/preconditioner/sor.hpp>
#include <ginkgo/core/reorder/amd.hpp>
#include <ginkgo/core/reorder/mc64.hpp>
#include <ginkgo/core/reorder/nested_dissection.hpp>
#include <ginkgo/core/reorder/rcm.hpp>
#include <ginkgo/core/reorder/reordering_base.hpp>
#include <ginkgo/core/reorder/scaled_reordered.hpp>
#include <ginkgo/core/solver/batch_bicgstab.hpp>
#include <ginkgo/core/solver/batch_cg.hpp>
#include <ginkgo/core/solver/batch_solver_base.hpp>
#include <ginkgo/core/solver/bicg.hpp>
#include <ginkgo/core/solver/bicgstab.hpp>
#include <ginkgo/core/solver/cb_gmres.hpp>
#include <ginkgo/core/solver/cg.hpp>
#include <ginkgo/core/solver/cgs.hpp>
#include <ginkgo/core/solver/chebyshev.hpp>
#include <ginkgo/core/solver/direct.hpp>
#include <ginkgo/core/solver/fcg.hpp>
#include <ginkgo/core/solver/gcr.hpp>
#include <ginkgo/core/solver/gmres.hpp>
#include <ginkgo/core/solver/idr.hpp>
#include <ginkgo/core/solver/ir.hpp>
#include <ginkgo/core/solver/minres.hpp>
#include <ginkgo/core/solver/multigrid.hpp>
#include <ginkgo/core/solver/pipe_cg.hpp>
#include <ginkgo/core/solver/solver_base.hpp>
#include <ginkgo/core/solver/solver_traits.hpp>
#include <ginkgo/core/solver/triangular.hpp>
#include <ginkgo/core/solver/workspace.hpp>
#include <ginkgo/core/stop/batch_stop_enum.hpp>
#include <ginkgo/core/stop/combined.hpp>
#include <ginkgo/core/stop/criterion.hpp>
#include <ginkgo/core/stop/iteration.hpp>
#include <ginkgo/core/stop/residual_norm.hpp>
#include <ginkgo/core/stop/stopping_status.hpp>
#include <ginkgo/core/stop/time.hpp>
#include <ginkgo/core/synthesizer/containers.hpp>
'''
subdir('include/ginkgo')

reference_src = [
  'reference/base/batch_multi_vector_kernels.cpp',
  'reference/base/device_matrix_data_kernels.cpp',
  'reference/base/event_kernels.cpp',
  'reference/base/index_set_kernels.cpp',
  'reference/base/scoped_device_id.cpp',
  'reference/base/version.cpp',
  'reference/components/absolute_array_kernels.cpp',
  'reference/components/fill_array_kernels.cpp',
  'reference/components/format_conversion_kernels.cpp',
  'reference/components/precision_conversion_kernels.cpp',
  'reference/components/prefix_sum_kernels.cpp',
  'reference/components/range_minimum_query_kernels.cpp',
  'reference/components/reduce_array_kernels.cpp',
  'reference/factorization/cholesky_kernels.cpp',
  'reference/factorization/elimination_forest_kernels.cpp',
  'reference/factorization/factorization_kernels.cpp',
  'reference/factorization/ic_kernels.cpp',
  'reference/factorization/ilu_kernels.cpp',
  'reference/factorization/lu_kernels.cpp',
  'reference/factorization/par_ic_kernels.cpp',
  'reference/factorization/par_ict_kernels.cpp',
  'reference/factorization/par_ilu_kernels.cpp',
  'reference/factorization/par_ilut_kernels.cpp',
  'reference/matrix/batch_csr_kernels.cpp',
  'reference/matrix/batch_dense_kernels.cpp',
  'reference/matrix/batch_ell_kernels.cpp',
  'reference/matrix/coo_kernels.cpp',
  'reference/matrix/csr_kernels.cpp',
  'reference/matrix/dense_kernels.cpp',
  'reference/matrix/diagonal_kernels.cpp',
  'reference/matrix/ell_kernels.cpp',
  'reference/matrix/fbcsr_kernels.cpp',
  'reference/matrix/fft_kernels.cpp',
  'reference/matrix/hybrid_kernels.cpp',
  'reference/matrix/permutation_kernels.cpp',
  'reference/matrix/scaled_permutation_kernels.cpp',
  'reference/matrix/sellp_kernels.cpp',
  'reference/matrix/sparsity_csr_kernels.cpp',
  'reference/multigrid/pgm_kernels.cpp',
  'reference/preconditioner/batch_jacobi_kernels.cpp',
  'reference/preconditioner/isai_kernels.cpp',
  'reference/preconditioner/jacobi_kernels.cpp',
  'reference/preconditioner/sor_kernels.cpp',
  'reference/reorder/rcm_kernels.cpp',
  'reference/solver/batch_bicgstab_kernels.cpp',
  'reference/solver/batch_cg_kernels.cpp',
  'reference/solver/bicg_kernels.cpp',
  'reference/solver/bicgstab_kernels.cpp',
  'reference/solver/cb_gmres_kernels.cpp',
  'reference/solver/cg_kernels.cpp',
  'reference/solver/cgs_kernels.cpp',
  'reference/solver/chebyshev_kernels.cpp',
  'reference/solver/common_gmres_kernels.cpp',
  'reference/solver/fcg_kernels.cpp',
  'reference/solver/gcr_kernels.cpp',
  'reference/solver/gmres_kernels.cpp',
  'reference/solver/idr_kernels.cpp',
  'reference/solver/ir_kernels.cpp',
  'reference/solver/lower_trs_kernels.cpp',
  'reference/solver/minres_kernels.cpp',
  'reference/solver/multigrid_kernels.cpp',
  'reference/solver/pipe_cg_kernels.cpp',
  'reference/solver/upper_trs_kernels.cpp',
  'reference/stop/criterion_kernels.cpp',
  'reference/stop/residual_norm_kernels.cpp',
]
reference_test_src = {
  'reference/test/base/array.cpp': 0,
  'reference/test/base/batch_multi_vector_kernels.cpp': 0,
  'reference/test/base/combination.cpp': 0,
  'reference/test/base/composition.cpp': 0,
  'reference/test/base/index_set.cpp': 0,
  'reference/test/base/perturbation.cpp': 0,
  'reference/test/base/utils.cpp': 0,
  'reference/test/components/absolute_array_kernels.cpp': 0,
  'reference/test/components/fill_array_kernels.cpp': 0,
  'reference/test/components/format_conversion_kernels.cpp': 0,
  'reference/test/components/precision_conversion_kernels.cpp': 0,
  'reference/test/components/prefix_sum_kernels.cpp': 0,
  'reference/test/components/reduce_array_kernels.cpp': 0,
  'reference/test/factorization/cholesky_kernels.cpp': 0,
  'reference/test/factorization/factorization.cpp': 0,
  'reference/test/factorization/ic_kernels.cpp': 0,
  'reference/test/factorization/ilu_kernels.cpp': 0,
  'reference/test/factorization/lu_kernels.cpp': 0,
  'reference/test/factorization/par_ic_kernels.cpp': 0,
  'reference/test/factorization/par_ict_kernels.cpp': 0,
  'reference/test/factorization/par_ilu_kernels.cpp': 0,
  'reference/test/factorization/par_ilut_kernels.cpp': 0,
  'reference/test/log/convergence.cpp': 0,
  'reference/test/matrix/batch_csr_kernels.cpp': 0,
  'reference/test/matrix/batch_dense_kernels.cpp': 0,
  'reference/test/matrix/batch_ell_kernels.cpp': 0,
  'reference/test/matrix/coo_kernels.cpp': 0,
  'reference/test/matrix/csr_kernels.cpp': 0,
  'reference/test/matrix/dense_kernels.cpp': 0,
  'reference/test/matrix/diagonal_kernels.cpp': 0,
  'reference/test/matrix/ell_kernels.cpp': 0,
  'reference/test/matrix/fbcsr_kernels.cpp': 0,
  'reference/test/matrix/fft_kernels.cpp': 0,
  'reference/test/matrix/hybrid_kernels.cpp': 0,
  'reference/test/matrix/identity.cpp': 0,
  'reference/test/matrix/permutation.cpp': 0,
  'reference/test/matrix/scaled_permutation.cpp': 0,
  'reference/test/matrix/sellp_kernels.cpp': 0,
  'reference/test/matrix/sparsity_csr.cpp': 0,
  'reference/test/matrix/sparsity_csr_kernels.cpp': 0,
  'reference/test/multigrid/fixed_coarsening_kernels.cpp': 0,
  'reference/test/multigrid/pgm_kernels.cpp': 0,
  'reference/test/preconditioner/batch_jacobi_kernels.cpp': 0,
  'reference/test/preconditioner/gauss_seidel.cpp': 0,
  'reference/test/preconditioner/ic.cpp': 0,
  'reference/test/preconditioner/ilu.cpp': 0,
  'reference/test/preconditioner/isai_kernels.cpp': 0,
  'reference/test/preconditioner/jacobi.cpp': 0,
  'reference/test/preconditioner/jacobi_kernels.cpp': 0,
  'reference/test/preconditioner/sor_kernels.cpp': 0,
  'reference/test/reorder/mc64.cpp': 0,
  'reference/test/reorder/mc64_kernels.cpp': 0,
  'reference/test/reorder/nested_dissection.cpp': 0,
  'reference/test/reorder/rcm.cpp': 0,
  'reference/test/reorder/rcm_kernels.cpp': 0,
  'reference/test/reorder/scaled_reordered.cpp': 0,
  'reference/test/solver/batch_bicgstab_kernels.cpp': 0,
  'reference/test/solver/batch_cg_kernels.cpp': 0,
  'reference/test/solver/bicg_kernels.cpp': 0,
  'reference/test/solver/bicgstab_kernels.cpp': 0,
  'reference/test/solver/cb_gmres_kernels.cpp': 0,
  'reference/test/solver/cg_kernels.cpp': 0,
  'reference/test/solver/cgs_kernels.cpp': 0,
  'reference/test/solver/chebyshev_kernels.cpp': 0,
  'reference/test/solver/direct.cpp': 0,
  'reference/test/solver/fcg_kernels.cpp': 0,
  'reference/test/solver/gcr_kernels.cpp': 0,
  'reference/test/solver/gmres_kernels.cpp': 0,
  'reference/test/solver/idr_kernels.cpp': 0,
  'reference/test/solver/ir_kernels.cpp': 0,
  'reference/test/solver/lower_trs.cpp': 0,
  'reference/test/solver/lower_trs_kernels.cpp': 0,
  'reference/test/solver/minres_kernels.cpp': 0,
  'reference/test/solver/multigrid_kernels.cpp': 0,
  'reference/test/solver/pipe_cg_kernels.cpp': 0,
  'reference/test/solver/upper_trs.cpp': 0,
  'reference/test/solver/upper_trs_kernels.cpp': 0,
  'reference/test/stop/combined.cpp': 0,
  'reference/test/stop/criterion_kernels.cpp': 0,
  'reference/test/stop/iteration.cpp': 0,
  'reference/test/stop/residual_norm_kernels.cpp': 0,
  'reference/test/stop/time.cpp': 0,
  'reference/test/utils/assertions_test.cpp': 0,
  # 'test/base/batch_multi_vector_kernels.cpp',
  'test/base/device_matrix_data_kernels.cpp': 0,
  'test/base/executor.cpp': 0,
  'test/base/timer.cpp': 0,
  'test/components/absolute_array_kernels.cpp': 0,
  'test/components/fill_array_kernels.cpp': 0,
  # 'test/components/format_conversion_kernels.cpp',
  'test/components/precision_conversion_kernels.cpp': 0,
  'test/components/prefix_sum_kernels.cpp': 0,
  'test/components/reduce_array_kernels.cpp': 0,
  'test/factorization/cholesky_kernels.cpp': 0,
  'test/factorization/factorization_kernels.cpp': 0,
  'test/factorization/ic_kernels.cpp': 0,
  'test/factorization/lu_kernels.cpp': 0,
  'test/factorization/par_ic_kernels.cpp': 0,
  'test/factorization/par_ict_kernels.cpp': 0,
  'test/factorization/par_ilu_kernels.cpp': 0,
  'test/factorization/par_ilut_kernels.cpp': 0,
  'test/log/profiler_hook.cpp': 0,
  'test/matrix/batch_csr_kernels.cpp': 0,
  'test/matrix/batch_dense_kernels.cpp': 0,
  'test/matrix/batch_ell_kernels.cpp': 0,
  'test/matrix/coo_kernels.cpp': 0,
  'test/matrix/dense_kernels.cpp': 0,
  'test/matrix/diagonal_kernels.cpp': 0,
  'test/matrix/ell_kernels.cpp': 0,
  'test/matrix/fbcsr_kernels.cpp': 0,
  'test/matrix/fft_kernels.cpp': 0,
  'test/matrix/hybrid_kernels.cpp': 0,
  'test/matrix/matrix.cpp': 0,
  'test/matrix/permutation_kernels.cpp': 0,
  'test/matrix/scaled_permutation_kernels.cpp': 0,
  'test/matrix/sellp_kernels.cpp': 0,
  'test/matrix/sparsity_csr_kernels.cpp': 0,
  'test/multigrid/fixed_coarsening_kernels.cpp': 0,
  'test/multigrid/pgm_kernels.cpp': 0,
  'test/preconditioner/batch_jacobi_kernels.cpp': 0,
  'test/preconditioner/isai_kernels.cpp': 0,
  'test/preconditioner/jacobi_kernels.cpp': 0,
  'test/preconditioner/sor_kernels.cpp': 0,
  'test/reorder/amd.cpp': 0,
  'test/reorder/mc64.cpp': 0,
  'test/reorder/nested_dissection.cpp': 0,
  'test/reorder/rcm.cpp': 0,
  'test/solver/batch_bicgstab_kernels.cpp': 0,
  'test/solver/batch_cg_kernels.cpp': 0,
  'test/solver/bicg_kernels.cpp': 0,
  'test/solver/bicgstab_kernels.cpp': 0,
  'test/solver/cb_gmres_kernels.cpp': 0,
  'test/solver/cg_kernels.cpp': 0,
  'test/solver/cgs_kernels.cpp': 0,
  'test/solver/chebyshev_kernels.cpp': 0,
  'test/solver/direct.cpp': 0,
  'test/solver/fcg_kernels.cpp': 0,
  'test/solver/gcr_kernels.cpp': 0,
  'test/solver/gmres_kernels.cpp': 0,
  'test/solver/idr_kernels.cpp': 0,
  'test/solver/ir_kernels.cpp': 0,
  'test/solver/lower_trs_kernels.cpp': 0,
  'test/solver/minres_kernels.cpp': 0,
  'test/solver/multigrid_kernels.cpp': 0,
  'test/solver/pipe_cg_kernels.cpp': 0,
  'test/solver/solver.cpp': 0,
  'test/solver/upper_trs_kernels.cpp': 0,
  'test/stop/combined_kernels.cpp': 0,
  'test/stop/criterion_kernels.cpp': 0,
  'test/stop/residual_norm_kernels.cpp': 0,
}
omp_src = [
  'omp/base/batch_multi_vector_kernels.cpp',
  'omp/base/device_matrix_data_kernels.cpp',
  'omp/base/event_kernels.cpp',
  'omp/base/executor.cpp',
  'omp/base/index_set_kernels.cpp',
  'omp/base/scoped_device_id.cpp',
  'omp/base/version.cpp',
  'omp/components/prefix_sum_kernels.cpp',
  'omp/factorization/cholesky_kernels.cpp',
  'omp/factorization/elimination_forest_kernels.cpp',
  'omp/factorization/factorization_kernels.cpp',
  'omp/factorization/ic_kernels.cpp',
  'omp/factorization/ilu_kernels.cpp',
  'omp/factorization/lu_kernels.cpp',
  'omp/factorization/par_ic_kernels.cpp',
  'omp/factorization/par_ict_kernels.cpp',
  'omp/factorization/par_ilu_kernels.cpp',
  'omp/factorization/par_ilut_kernels.cpp',
  'omp/matrix/batch_csr_kernels.cpp',
  'omp/matrix/batch_dense_kernels.cpp',
  'omp/matrix/batch_ell_kernels.cpp',
  'omp/matrix/coo_kernels.cpp',
  'omp/matrix/csr_kernels.cpp',
  'omp/matrix/dense_kernels.cpp',
  'omp/matrix/diagonal_kernels.cpp',
  'omp/matrix/ell_kernels.cpp',
  'omp/matrix/fbcsr_kernels.cpp',
  'omp/matrix/fft_kernels.cpp',
  'omp/matrix/sellp_kernels.cpp',
  'omp/matrix/sparsity_csr_kernels.cpp',
  'omp/multigrid/pgm_kernels.cpp',
  'omp/preconditioner/batch_jacobi_kernels.cpp',
  'omp/preconditioner/isai_kernels.cpp',
  'omp/preconditioner/jacobi_kernels.cpp',
  'omp/preconditioner/sor_kernels.cpp',
  'omp/reorder/rcm_kernels.cpp',
  'omp/solver/batch_bicgstab_kernels.cpp',
  'omp/solver/batch_cg_kernels.cpp',
  'omp/solver/cb_gmres_kernels.cpp',
  'omp/solver/idr_kernels.cpp',
  'omp/solver/lower_trs_kernels.cpp',
  'omp/solver/multigrid_kernels.cpp',
  'omp/solver/upper_trs_kernels.cpp',
  'omp/stop/criterion_kernels.cpp',
  'omp/stop/residual_norm_kernels.cpp',
  'common/unified/base/device_matrix_data_kernels.cpp',
  'common/unified/base/index_set_kernels.cpp',
  'common/unified/components/absolute_array_kernels.cpp',
  'common/unified/components/fill_array_kernels.cpp',
  'common/unified/components/format_conversion_kernels.cpp',
  'common/unified/components/precision_conversion_kernels.cpp',
  'common/unified/components/range_minimum_query_kernels.cpp',
  'common/unified/components/reduce_array_kernels.cpp',
  'common/unified/matrix/coo_kernels.cpp',
  'common/unified/matrix/csr_kernels.cpp',
  'common/unified/matrix/dense_kernels.instantiate.cpp',
  'common/unified/matrix/dense_kernels.template.cpp',
  'common/unified/matrix/diagonal_kernels.cpp',
  'common/unified/matrix/ell_kernels.cpp',
  'common/unified/matrix/hybrid_kernels.cpp',
  'common/unified/matrix/permutation_kernels.cpp',
  'common/unified/matrix/scaled_permutation_kernels.cpp',
  'common/unified/matrix/sellp_kernels.cpp',
  'common/unified/matrix/sparsity_csr_kernels.cpp',
  'common/unified/multigrid/pgm_kernels.cpp',
  'common/unified/preconditioner/jacobi_kernels.cpp',
  'common/unified/solver/bicg_kernels.cpp',
  'common/unified/solver/bicgstab_kernels.cpp',
  'common/unified/solver/cg_kernels.cpp',
  'common/unified/solver/cgs_kernels.cpp',
  'common/unified/solver/chebyshev_kernels.cpp',
  'common/unified/solver/common_gmres_kernels.cpp',
  'common/unified/solver/fcg_kernels.cpp',
  'common/unified/solver/gcr_kernels.cpp',
  'common/unified/solver/gmres_kernels.cpp',
  'common/unified/solver/ir_kernels.cpp',
  'common/unified/solver/minres_kernels.cpp',
  'common/unified/solver/pipe_cg_kernels.cpp',
]
omp_test_src = {
  'omp/test/base/index_set.cpp': 0,
  'omp/test/base/kernel_launch.cpp': 0,
  'omp/test/matrix/fbcsr_kernels.cpp': 0,
  'test/base/batch_multi_vector_kernels.cpp': 0,
  'test/base/device_matrix_data_kernels.cpp': 0,
  'test/base/executor.cpp': 0,
  'test/base/highest_precision.cpp': 0,
  'test/base/index_range.cpp': 0,
  'test/base/intrinsics.cpp': 0,
  'test/base/iterator_factory.cpp': 0,
  'test/base/kernel_launch_generic.cpp': 0,
  'test/base/segmented_range.cpp': 0,
  'test/base/timer.cpp': 0,
  'test/components/absolute_array_kernels.cpp': 0,
  'test/components/bitvector.cpp': 0,
  'test/components/fill_array_kernels.cpp': 0,
  'test/components/format_conversion_kernels.cpp': 0,
  'test/components/precision_conversion_kernels.cpp': 0,
  'test/components/prefix_sum_kernels.cpp': 0,
  'test/components/range_minimum_query_kernels.cpp': 0,
  'test/components/reduce_array_kernels.cpp': 0,
  'test/factorization/cholesky_kernels.cpp': 0,
  'test/factorization/factorization_kernels.cpp': 0,
  'test/factorization/ic_kernels.cpp': 0,
  'test/factorization/ilu_kernels.cpp': 0,
  'test/factorization/lu_kernels.cpp': 0,
  'test/factorization/par_ic_kernels.cpp': 0,
  'test/factorization/par_ict_kernels.cpp': 0,
  'test/factorization/par_ilu_kernels.cpp': 0,
  'test/factorization/par_ilut_kernels.cpp': 0,
  'test/log/profiler_hook.cpp': 0,
  'test/matrix/batch_csr_kernels.cpp': 0,
  'test/matrix/batch_dense_kernels.cpp': 0,
  'test/matrix/batch_ell_kernels.cpp': 0,
  'test/matrix/coo_kernels.cpp': 0,
  'test/matrix/csr_kernels2.cpp': 0,
  'test/matrix/csr_kernels.cpp': 0,
  'test/matrix/dense_kernels.cpp': 0,
  'test/matrix/diagonal_kernels.cpp': 0,
  'test/matrix/ell_kernels.cpp': 0,
  'test/matrix/fbcsr_kernels.cpp': 0,
  'test/matrix/fft_kernels.cpp': 0,
  'test/matrix/hybrid_kernels.cpp': 0,
  'test/matrix/matrix.cpp': 0,
  'test/matrix/permutation_kernels.cpp': 0,
  'test/matrix/scaled_permutation_kernels.cpp': 0,
  'test/matrix/sellp_kernels.cpp': 0,
  'test/matrix/sparsity_csr_kernels.cpp': 0,
  'test/multigrid/fixed_coarsening_kernels.cpp': 0,
  'test/multigrid/pgm_kernels.cpp': 0,
  'test/preconditioner/batch_jacobi_kernels.cpp': 0,
  'test/preconditioner/isai_kernels.cpp': 0,
  'test/preconditioner/jacobi_kernels.cpp': 0,
  'test/preconditioner/sor_kernels.cpp': 0,
  'test/reorder/amd.cpp': 0,
  'test/reorder/mc64.cpp': 0,
  'test/reorder/nested_dissection.cpp': 0,
  'test/reorder/rcm.cpp': 0,
  'test/solver/batch_bicgstab_kernels.cpp': 0,
  'test/solver/batch_cg_kernels.cpp': 0,
  'test/solver/bicg_kernels.cpp': 0,
  'test/solver/bicgstab_kernels.cpp': 0,
  'test/solver/cb_gmres_kernels.cpp': 0,
  'test/solver/cg_kernels.cpp': 0,
  'test/solver/cgs_kernels.cpp': 0,
  'test/solver/chebyshev_kernels.cpp': 0,
  'test/solver/direct.cpp': 0,
  'test/solver/fcg_kernels.cpp': 0,
  'test/solver/gcr_kernels.cpp': 0,
  'test/solver/gmres_kernels.cpp': 0,
  'test/solver/idr_kernels.cpp': 0,
  'test/solver/ir_kernels.cpp': 0,
  'test/solver/lower_trs_kernels.cpp': 0,
  'test/solver/minres_kernels.cpp': 0,
  'test/solver/multigrid_kernels.cpp': 0,
  'test/solver/pipe_cg_kernels.cpp': 0,
  'test/solver/solver.cpp': 0,
  'test/solver/upper_trs_kernels.cpp': 0,
  'test/stop/combined_kernels.cpp': 0,
  'test/stop/criterion_kernels.cpp': 0,
  'test/stop/residual_norm_kernels.cpp': 0,
}
devices_src = [
  'core/device_hooks/cuda_hooks.cpp',
  'core/device_hooks/dpcpp_hooks.cpp',
  'core/device_hooks/hip_hooks.cpp',
  'devices/cuda/executor.cpp',
  'devices/device.cpp',
  'devices/dpcpp/executor.cpp',
  'devices/hip/executor.cpp',
  'devices/machine_topology.cpp',
  'devices/omp/executor.cpp',
  'devices/reference/dummy.cpp',
]
core_src = [
  'core/base/array.cpp',
  'core/base/batch_multi_vector.cpp',
  'core/base/block_operator.cpp',
  'core/base/combination.cpp',
  'core/base/composition.cpp',
  'core/base/dense_cache.cpp',
  'core/base/device_matrix_data.cpp',
  'core/base/executor.cpp',
  'core/base/index_set.cpp',
  'core/base/memory.cpp',
  'core/base/mtx_io.cpp',
  'core/base/perturbation.cpp',
  'core/base/segmented_array.cpp',
  'core/base/timer.cpp',
  'core/base/version.cpp',
  'core/components/range_minimum_query.cpp',
  'core/config/config.cpp',
  'core/config/config_helper.cpp',
  'core/config/factorization_config.cpp',
  'core/config/multigrid_config.cpp',
  'core/config/preconditioner_config.cpp',
  'core/config/preconditioner_ic_config.cpp',
  'core/config/preconditioner_ilu_config.cpp',
  'core/config/preconditioner_isai_config.cpp',
  'core/config/property_tree.cpp',
  'core/config/registry.cpp',
  'core/config/solver_config.cpp',
  'core/config/stop_config.cpp',
  'core/config/type_descriptor.cpp',
  'core/factorization/cholesky.cpp',
  'core/factorization/elimination_forest.cpp',
  'core/factorization/factorization.cpp',
  'core/factorization/ic.cpp',
  'core/factorization/ilu.cpp',
  'core/factorization/lu.cpp',
  'core/factorization/par_ic.cpp',
  'core/factorization/par_ict.cpp',
  'core/factorization/par_ilu.cpp',
  'core/factorization/par_ilut.cpp',
  'core/factorization/symbolic.cpp',
  'core/log/batch_logger.cpp',
  'core/log/convergence.cpp',
  'core/log/logger.cpp',
  'core/log/performance_hint.cpp',
  'core/log/profiler_hook.cpp',
  'core/log/profiler_hook_summary.cpp',
  'core/log/profiler_hook_summary_writer.cpp',
  'core/log/record.cpp',
  'core/log/solver_progress.cpp',
  'core/log/stream.cpp',
  'core/log/tau.cpp',
  'core/log/vtune.cpp',
  'core/matrix/batch_csr.cpp',
  'core/matrix/batch_dense.cpp',
  'core/matrix/batch_ell.cpp',
  'core/matrix/batch_identity.cpp',
  'core/matrix/coo.cpp',
  'core/matrix/csr.cpp',
  'core/matrix/csr_lookup.cpp',
  'core/matrix/dense.cpp',
  'core/matrix/diagonal.cpp',
  'core/matrix/ell.cpp',
  'core/matrix/fbcsr.cpp',
  'core/matrix/fft.cpp',
  'core/matrix/hybrid.cpp',
  'core/matrix/identity.cpp',
  'core/matrix/permutation.cpp',
  'core/matrix/row_gatherer.cpp',
  'core/matrix/scaled_permutation.cpp',
  'core/matrix/sellp.cpp',
  'core/matrix/sparsity_csr.cpp',
  'core/multigrid/fixed_coarsening.cpp',
  'core/multigrid/pgm.cpp',
  'core/preconditioner/batch_jacobi.cpp',
  'core/preconditioner/gauss_seidel.cpp',
  'core/preconditioner/ic.cpp',
  'core/preconditioner/ilu.cpp',
  'core/preconditioner/isai.cpp',
  'core/preconditioner/jacobi.cpp',
  'core/preconditioner/sor.cpp',
  'core/reorder/amd.cpp',
  'core/reorder/mc64.cpp',
  'core/reorder/nested_dissection.cpp',
  'core/reorder/rcm.cpp',
  'core/reorder/scaled_reordered.cpp',
  'core/solver/batch_bicgstab.cpp',
  'core/solver/batch_cg.cpp',
  'core/solver/bicg.cpp',
  'core/solver/bicgstab.cpp',
  'core/solver/cb_gmres.cpp',
  'core/solver/cg.cpp',
  'core/solver/cgs.cpp',
  'core/solver/chebyshev.cpp',
  'core/solver/direct.cpp',
  'core/solver/fcg.cpp',
  'core/solver/gcr.cpp',
  'core/solver/gmres.cpp',
  'core/solver/idr.cpp',
  'core/solver/ir.cpp',
  'core/solver/lower_trs.cpp',
  'core/solver/minres.cpp',
  'core/solver/multigrid.cpp',
  'core/solver/pipe_cg.cpp',
  'core/solver/upper_trs.cpp',
  'core/stop/combined.cpp',
  'core/stop/criterion.cpp',
  'core/stop/iteration.cpp',
  'core/stop/residual_norm.cpp',
  'core/stop/time.cpp',
  'third_party/SuiteSparse/wrapper32.cpp',
  'third_party/SuiteSparse/wrapper64.cpp',
]
core_test_src = {
  'core/test/accessor/block_col_major.cpp': 0,
  'core/test/accessor/index_span.cpp': 0,
  'core/test/accessor/math.cpp': 0,
  'core/test/accessor/range.cpp': 0,
  'core/test/accessor/reduced_row_major.cpp': 0,
  'core/test/accessor/reduced_row_major_ginkgo.cpp': 0,
  'core/test/accessor/reduced_row_major_reference.cpp': 0,
  'core/test/accessor/row_major.cpp': 0,
  'core/test/accessor/scaled_reduced_row_major.cpp': 0,
  'core/test/accessor/scaled_reduced_row_major_reference.cpp': 0,
  'core/test/base/abstract_factory.cpp': 0,
  'core/test/base/allocator.cpp': 0,
  'core/test/base/array.cpp': 0,
  'core/test/base/batch_dim.cpp': 0,
  'core/test/base/batch_lin_op.cpp': 0,
  'core/test/base/batch_multi_vector.cpp': 0,
  'core/test/base/bfloat16.cpp': 0,
  'core/test/base/block_operator.cpp': 0,
  'core/test/base/combination.cpp': 0,
  'core/test/base/composition.cpp': 0,
  'core/test/base/deferred_factory.cpp': 0,
  'core/test/base/dense_cache.cpp': 0,
  'core/test/base/dim.cpp': 0,
  'core/test/base/exception.cpp': 0,
  'core/test/base/exception_helpers.cpp': 0,
  'core/test/base/executor.cpp': 0,
  'core/test/base/extended_float.cpp': 0,
  'core/test/base/half.cpp': 0,
  'core/test/base/highest_precision.cpp': 0,
  'core/test/base/index_range.cpp': 0,
  'core/test/base/iterator_factory.cpp': 0,
  'core/test/base/lin_op.cpp': 0,
  'core/test/base/math.cpp': 0,
  'core/test/base/matrix_assembly_data.cpp': 0,
  'core/test/base/matrix_data.cpp': 0,
  'core/test/base/mtx_io.cpp': 0,
  'core/test/base/perturbation.cpp': 0,
  'core/test/base/polymorphic_object.cpp': 0,
  'core/test/base/range_accessors.cpp': 0,
  'core/test/base/range.cpp': 0,
  'core/test/base/sanitizers.cpp': 0,
  'core/test/base/segmented_array.cpp': 0,
  'core/test/base/segmented_range.cpp': 0,
  'core/test/base/types.cpp': 0,
  'core/test/base/utils.cpp': 0,
  'core/test/base/version.cpp': 0,
  'core/test/components/addressable_pq.cpp': 0,
  'core/test/components/bit_packed_storage.cpp': 0,
  'core/test/components/disjoint_sets.cpp': 0,
  'core/test/components/range_minimum_query.cpp': 0,
  'core/test/config/config.cpp': 0,
  'core/test/config/factorization.cpp': 0,
  'core/test/config/multigrid.cpp': 0,
  'core/test/config/preconditioner.cpp': 0,
  'core/test/config/property_tree.cpp': 0,
  'core/test/config/registry.cpp': 0,
  'core/test/config/solver.cpp': 0,
  'core/test/config/type_descriptor.cpp': 0,
  'core/test/factorization/elimination_forest.cpp': 0,
  'core/test/factorization/par_ic.cpp': 0,
  'core/test/factorization/par_ict.cpp': 0,
  'core/test/factorization/par_ilu.cpp': 0,
  'core/test/factorization/par_ilut.cpp': 0,
  'core/test/log/convergence.cpp': 0,
  'core/test/log/logger.cpp': 0,
  'core/test/log/performance_hint.cpp': 0,
  'core/test/log/profiler_hook.cpp': 0,
  'core/test/log/record.cpp': 0,
  'core/test/log/solver_progress.cpp': 0,
  'core/test/log/stream.cpp': 0,
  'core/test/matrix/batch_csr.cpp': 0,
  'core/test/matrix/batch_dense.cpp': 0,
  'core/test/matrix/batch_ell.cpp': 0,
  'core/test/matrix/batch_identity.cpp': 0,
  'core/test/matrix/coo_builder.cpp': 0,
  'core/test/matrix/coo.cpp': 0,
  'core/test/matrix/csr_builder.cpp': 0,
  'core/test/matrix/csr.cpp': 0,
  'core/test/matrix/dense.cpp': 0,
  'core/test/matrix/diagonal.cpp': 0,
  'core/test/matrix/ell.cpp': 0,
  'core/test/matrix/fbcsr_builder.cpp': 0,
  'core/test/matrix/fbcsr.cpp': 0,
  'core/test/matrix/hybrid.cpp': 0,
  'core/test/matrix/identity.cpp': 0,
  'core/test/matrix/permutation.cpp': 0,
  'core/test/matrix/row_gatherer.cpp': 0,
  'core/test/matrix/sellp.cpp': 0,
  'core/test/matrix/sparsity_csr.cpp': 0,
  'core/test/multigrid/fixed_coarsening.cpp': 0,
  'core/test/multigrid/pgm.cpp': 0,
  'core/test/preconditioner/batch_jacobi.cpp': 0,
  'core/test/preconditioner/gauss_seidel.cpp': 0,
  'core/test/preconditioner/ic.cpp': 0,
  'core/test/preconditioner/ilu.cpp': 0,
  'core/test/preconditioner/isai.cpp': 0,
  'core/test/preconditioner/jacobi.cpp': 0,
  'core/test/preconditioner/sor.cpp': 0,
  'core/test/reorder/amd.cpp': 0,
  'core/test/reorder/nested_dissection.cpp': 0,
  'core/test/reorder/rcm.cpp': 0,
  'core/test/reorder/scaled_reordered.cpp': 0,
  'core/test/solver/batch_bicgstab.cpp': 0,
  'core/test/solver/batch_cg.cpp': 0,
  'core/test/solver/bicg.cpp': 0,
  'core/test/solver/bicgstab.cpp': 0,
  'core/test/solver/cb_gmres.cpp': 0,
  'core/test/solver/cg.cpp': 0,
  'core/test/solver/cgs.cpp': 0,
  'core/test/solver/chebyshev.cpp': 0,
  'core/test/solver/direct.cpp': 0,
  'core/test/solver/fcg.cpp': 0,
  'core/test/solver/gcr.cpp': 0,
  'core/test/solver/gmres.cpp': 0,
  'core/test/solver/idr.cpp': 0,
  'core/test/solver/ir.cpp': 0,
  'core/test/solver/lower_trs.cpp': 0,
  'core/test/solver/multigrid.cpp': 0,
  'core/test/solver/pipe_cg.cpp': 0,
  'core/test/solver/upper_trs.cpp': 0,
  'core/test/solver/workspace.cpp': 0,
  'core/test/stop/combined.cpp': 0,
  'core/test/stop/criterion.cpp': 0,
  'core/test/stop/iteration.cpp': 0,
  'core/test/stop/stopping_status.cpp': 0,
  'core/test/stop/time.cpp': 0,
  'core/test/utils/array_generator_test.cpp': 0,
  'core/test/utils/assertions_test.cpp': 0,
  'core/test/utils/fb_matrix_generator_test.cpp': 0,
  'core/test/utils/matrix_generator_test.cpp': 0,
  'core/test/utils/matrix_utils_test.cpp': 0,
  'core/test/utils/unsort_matrix_test.cpp': 0,
  'core/test/utils/utils_test.cpp': 0,
  'core/test/utils/value_generator_test.cpp': 0,
}

if with_mpi
  reference_src += [
    'reference/distributed/assembly_kernels.cpp',
    'reference/distributed/index_map_kernels.cpp',
    'reference/distributed/matrix_kernels.cpp',
    'reference/distributed/partition_helpers_kernels.cpp',
    'reference/distributed/partition_kernels.cpp',
    'reference/distributed/vector_kernels.cpp',
  ]
  reference_test_src += {
    'reference/test/distributed/assembly_kernels.cpp': 3,
    'reference/test/distributed/index_map_kernels.cpp': 3,
    'reference/test/distributed/matrix_kernels.cpp': 3,
    'reference/test/distributed/partition_helpers_kernels.cpp': 3,
    'reference/test/distributed/partition_kernels.cpp': 3,
    'reference/test/distributed/vector_kernels.cpp': 3,
    'test/distributed/assembly_kernels.cpp': 3,
    'test/distributed/index_map_kernels.cpp': 3,
    'test/distributed/matrix_kernels.cpp': 3,
    'test/distributed/partition_helper_kernels.cpp': 3,
    'test/distributed/partition_kernels.cpp': 3,
    'test/distributed/vector_kernels.cpp': 3,
    'test/mpi/distributed/assembly.cpp': 3,
    'test/mpi/distributed/matrix.cpp': 3,
    'test/mpi/distributed/partition_helpers.cpp': 3,
    'test/mpi/distributed/row_gatherer.cpp': 6,
    'test/mpi/distributed/vector.cpp': 3,
    'test/mpi/multigrid/pgm.cpp': 3,
    'test/mpi/preconditioner/schwarz.cpp': 3,
    'test/mpi/solver/solver.cpp': 3,
  }
  omp_src += [
    'omp/distributed/assembly_kernels.cpp',
    'omp/distributed/index_map_kernels.cpp',
    'omp/distributed/matrix_kernels.cpp',
    'omp/distributed/partition_helpers_kernels.cpp',
    'omp/distributed/partition_kernels.cpp',
    'omp/distributed/vector_kernels.cpp',
    'common/unified/distributed/assembly_kernels.cpp',
    'common/unified/distributed/partition_helpers_kernels.cpp',
    'common/unified/distributed/partition_kernels.cpp',
  ]
  omp_test_src += {
    'test/distributed/assembly_kernels.cpp': 3,
    'test/distributed/index_map_kernels.cpp': 3,
    'test/distributed/matrix_kernels.cpp': 3,
    'test/distributed/partition_helper_kernels.cpp': 3,
    'test/distributed/partition_kernels.cpp': 3,
    'test/distributed/vector_kernels.cpp': 3,
    'test/mpi/distributed/assembly.cpp': 3,
    'test/mpi/distributed/matrix.cpp': 3,
    'test/mpi/distributed/partition_helpers.cpp': 3,
    'test/mpi/distributed/row_gatherer.cpp': 6,
    'test/mpi/distributed/vector.cpp': 3,
    'test/mpi/multigrid/pgm.cpp': 3,
    'test/mpi/preconditioner/schwarz.cpp': 3,
    'test/mpi/solver/solver.cpp': 3,
  }
  core_src += [
    'core/base/mpi.cpp',
    'core/config/schwarz_config.cpp',
    'core/distributed/assembly.cpp',
    'core/distributed/collective_communicator.cpp',
    'core/distributed/dense_communicator.cpp',
    'core/distributed/index_map.cpp',
    'core/distributed/matrix.cpp',
    'core/distributed/neighborhood_communicator.cpp',
    'core/distributed/partition.cpp',
    'core/distributed/partition_helpers.cpp',
    'core/distributed/preconditioner/schwarz.cpp',
    'core/distributed/row_gatherer.cpp',
    'core/distributed/vector_cache.cpp',
    'core/distributed/vector.cpp',
    'core/mpi/exception.cpp',
  ]
  core_test_src += {
    'core/test/distributed/index_map.cpp': 3,
    'core/test/mpi/base/bindings.cpp': 4,
    'core/test/mpi/base/communicator.cpp': 8,
    'core/test/mpi/base/exception_helpers.cpp': 3,
    'core/test/mpi/base/rank_mapping.cpp': 4,
    'core/test/mpi/distributed/collective_communicator.cpp': 6,
    'core/test/mpi/distributed/helpers.cpp': 3,
    'core/test/mpi/distributed/matrix.cpp': 3,
    'core/test/mpi/distributed/preconditioner/schwarz.cpp': 3,
    'core/test/mpi/distributed/row_gatherer.cpp': 6,
    'core/test/mpi/distributed/solver/multigrid.cpp': 3,
    'core/test/mpi/distributed/vector_cache.cpp': 3,
  }
endif

reference_lib = library(
  'ginkgo_reference',
  reference_src,
  include_directories: include_directories('include'),
  cpp_args: ['-DGKO_DEVICE_NAMESPACE=reference'],
)
omp_lib = library(
  'ginkgo_omp',
  omp_src,
  include_directories: include_directories('include'),
  dependencies: omp_dep,
  cpp_args: ['-DGKO_COMPILING_OMP', '-DGKO_DEVICE_NAMESPACE=omp'],
)
ginkgo_lib = library(
  'ginkgo',
  core_src + devices_src,
  dependencies: [hwloc_dep, metis_dep, mpi_dep],
  link_with: [omp_lib, reference_lib],
  include_directories: include_directories('include'),
)
ginkgo_dep = declare_dependency(
  link_with: [ginkgo_lib, omp_lib, reference_lib],
  dependencies: [metis_dep, mpi_dep, omp_dep],
  include_directories: include_directories('include'),
)

if get_option('examples')
  subdir('examples')
endif

# tests
if get_option('tests')
  gtest_dep = dependency('gtest')
  ginkgo_test_srcs = [
    ['core/test/gtest/ginkgo_main.cpp', 'core/test/gtest/resources.cpp'],
    ['core/test/gtest/ginkgo_mpi_main.cpp', 'core/test/gtest/resources.cpp'],
  ]

  build_dir = meson.current_build_dir()
  subdir('matrices')
  foreach cpp, pnum : reference_test_src
    is_mpi = pnum > 0
    if not is_mpi or with_mpi
      name = '_'.join(cpp.split('/')).split('.')[0]
      exe = executable(
        f'reference_@name@',
        [cpp] + ginkgo_test_srcs[is_mpi],
        dependencies: [ginkgo_dep, gtest_dep],
        cpp_args: [
          '-DEXEC_TYPE=ReferenceExecutor',
          '-DGKO_COMPILING_REFERENCE',
          '-DGKO_DEVICE_NAMESPACE=reference',
        ],
      )
      if is_mpi
        test(
          name,
          mpirun,
          args: ['-n', pnum.to_string(), exe],
          suite: 'reference',
        )
      else
        test(name, exe, suite: 'reference')
      endif
    endif
  endforeach
  foreach cpp, pnum : omp_test_src
    is_mpi = pnum > 0
    if not is_mpi or with_mpi
      name = '_'.join(cpp.split('/')).split('.')[0]
      exe = executable(
        f'omp_@name@',
        [cpp] + ginkgo_test_srcs[cpp.contains('mpi')],
        dependencies: [ginkgo_dep, gtest_dep],
        cpp_args: [
          '-DEXEC_TYPE=OmpExecutor',
          '-DGKO_COMPILING_OMP',
          '-DGKO_DEVICE_NAMESPACE=omp',
        ],
      )
      if is_mpi
        test(
          name,
          mpirun,
          args: ['-n', pnum.to_string(), exe],
          suite: 'omp',
          env: {'OMP_NUM_THREADS': '3'},
        )
      else
        test(name, exe, suite: 'omp')
      endif
    endif
  endforeach
  foreach cpp, pnum : core_test_src
    is_mpi = pnum > 0
    if not is_mpi or with_mpi
      name = '_'.join(cpp.split('/')).split('.')[0]
      exe = executable(
        f'core_@name@',
        [cpp] + ginkgo_test_srcs[cpp.contains('mpi')],
        dependencies: [ginkgo_dep, gtest_dep],
      )
      if is_mpi
        test(name, mpirun, args: ['-n', pnum.to_string(), exe], suite: 'core')
      else
        test(name, exe, suite: 'core')
      endif
    endif
  endforeach
endif
