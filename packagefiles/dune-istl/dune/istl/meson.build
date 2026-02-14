# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# TODO Some tests have been disabled
foreach name, info : {
  'BCRSAssign': ['test/bcrsassigntest.cc', true],
  'BCRSBuild': ['test/bcrsbuild.cc', true],
  'BCRSImplicitbuild': ['test/bcrsimplicitbuild.cc', true],
  'BCRSMatrix': ['test/bcrsmatrixtest.cc', true],
  'BCRSNorm': ['test/bcrsnormtest.cc', true],
  'BlockLevel': ['test/blocklevel.cc', true],
  'BVector': ['test/bvectortest.cc', true],
  'CGCondition': ['test/cgconditiontest.cc', true],
  'CholMod': ['test/cholmodtest.cc', true],
  'ComplexMatrix': ['test/complexmatrixtest.cc', true],
  'ComplexRHS': ['test/complexrhstest.cc', false],
  'DotProduct': ['test/dotproducttest.cc', true],
  'FieldVector': ['test/fieldvectortest.cc', true],
  'ForEach': ['test/foreachtest.cc', true],
  'IluIldl': ['test/iluildltest.cc', true],
  'InverseOperator2Prec': ['test/inverseoperator2prectest.cc', true],
  'IO': ['test/iotest.cc', true],
  'Ldl': ['test/ldltest.cc', true],
  'MatrixIterator': ['test/matrixiteratortest.cc', true],
  'MatrixMarket': ['test/matrixmarkettest.cc', true],
  'MatrixNorm': ['test/matrixnormtest.cc', true],
  'MatrixRedist': ['test/matrixredisttest.cc', true],
  'Matrix': ['test/matrixtest.cc', true],
  'MatrixUtils': ['test/matrixutilstest.cc', true],
  'Mm': ['test/mmtest.cc', true],
  'MultiRhs': ['test/multirhstest.cc', false],
  'MultiTypeBlockMatrix': ['test/multitypeblockmatrixtest.cc', true],
  'MultiTypeBlockVector': ['test/multitypeblockvectortest.cc', true],
  'Mv': ['test/mv.cc', true],
  'OverlappingSchwarz': ['test/overlappingschwarztest.cc', true],
  'Preconditioners': ['test/preconditionerstest.cc', true],
  'Registry': ['test/registrytest.cc', true],
  'ScalarProducts': ['test/scalarproductstest.cc', true],
  'ScaleDidMatrix': ['test/scaledidmatrixtest.cc', true],
  'SolverAbort': ['test/solveraborttest.cc', true],
  'Solver': ['test/solvertest.cc', true],
  'Spqr': ['test/spqrtest.cc', true],
  'SuperLU': ['test/superlutest.cc', true],
  'UmfPack': ['test/umfpacktest.cc', true],
  'VbVector': ['test/vbvectortest.cc', true],
  'VectorComm': ['test/vectorcommtest.cc', true],
  'Cond2': ['eigenvalue/test/cond2test.cc', true],
  'AMG': ['paamg/test/amgtest.cc', true],
  'FastAMG': ['paamg/test/fastamg.cc', true],
  'Galerkin': ['paamg/test/galerkintest.cc', true],
  'Graph': ['paamg/test/graphtest.cc', true],
  'Hierarchy': ['paamg/test/hierarchytest.cc', true],
  'KAMG': ['paamg/test/kamgtest.cc', true],
  'PAMGMM': ['paamg/test/pamgmmtest.cc', true],
  'ParallelAMG': ['paamg/test/parallelamgtest.cc', true],
  'PThreadAMG': ['paamg/test/pthreadamgtest.cc', false],
  'PThreadTwoLevel': ['paamg/test/pthreadtwoleveltest.cc', true],
  'Transfer': ['paamg/test/transfertest.cc', true],
  'TwoLevelMethod': ['paamg/test/twolevelmethodtest.cc', true],
}
  sources = info[0]
  is_enabled = info[1]
  if is_enabled
    test(
      name,
      executable(
        name + 'Test',
        sources,
        dependencies: [dune_istl_dep],
      ),
    )
  endif
endforeach
