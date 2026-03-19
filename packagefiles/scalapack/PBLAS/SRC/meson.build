# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

subdir('PBBLAS')
subdir('PTZBLAS')
subdir('PTOOLS')

appblas = files('pilaenv.f')

piblas1 = files('picopy_.c')

psblas1 = files(
  'psamax_.c',
  'psasum_.c',
  'psaxpy_.c',
  'pscopy_.c',
  'psdot_.c',
  'psnrm2_.c',
  'psscal_.c',
  'psswap_.c',
)

pcblas1 = files(
  'pcamax_.c',
  'pcaxpy_.c',
  'pccopy_.c',
  'pcdotc_.c',
  'pcdotu_.c',
  'pcscal_.c',
  'pcsscal_.c',
  'pcswap_.c',
  'pscasum_.c',
  'pscnrm2_.c',
)

pdblas1 = files(
  'pdamax_.c',
  'pdasum_.c',
  'pdaxpy_.c',
  'pdcopy_.c',
  'pddot_.c',
  'pdnrm2_.c',
  'pdscal_.c',
  'pdswap_.c',
)

pzblas1 = files(
  'pdzasum_.c',
  'pdznrm2_.c',
  'pzamax_.c',
  'pzaxpy_.c',
  'pzcopy_.c',
  'pzdotc_.c',
  'pzdotu_.c',
  'pzdscal_.c',
  'pzscal_.c',
  'pzswap_.c',
)

psblas2 = files(
  'psagemv_.c',
  'psasymv_.c',
  'psatrmv_.c',
  'psgemv_.c',
  'psger_.c',
  'pssymv_.c',
  'pssyr2_.c',
  'pssyr_.c',
  'pstrmv_.c',
  'pstrsv_.c',
)

pcblas2 = files(
  'pcagemv_.c',
  'pcahemv_.c',
  'pcatrmv_.c',
  'pcgemv_.c',
  'pcgerc_.c',
  'pcgeru_.c',
  'pchemv_.c',
  'pcher2_.c',
  'pcher_.c',
  'pctrmv_.c',
  'pctrsv_.c',
)

pdblas2 = files(
  'pdagemv_.c',
  'pdasymv_.c',
  'pdatrmv_.c',
  'pdgemv_.c',
  'pdger_.c',
  'pdsymv_.c',
  'pdsyr2_.c',
  'pdsyr_.c',
  'pdtrmv_.c',
  'pdtrsv_.c',
)

pzblas2 = files(
  'pzagemv_.c',
  'pzahemv_.c',
  'pzatrmv_.c',
  'pzgemv_.c',
  'pzgerc_.c',
  'pzgeru_.c',
  'pzhemv_.c',
  'pzher2_.c',
  'pzher_.c',
  'pztrmv_.c',
  'pztrsv_.c',
)

psblas3 = files(
  'psgeadd_.c',
  'psgemm_.c',
  'pssymm_.c',
  'pssyr2k_.c',
  'pssyrk_.c',
  'pstradd_.c',
  'pstran_.c',
  'pstrmm_.c',
  'pstrsm_.c',
)

pcblas3 = files(
  'pcgeadd_.c',
  'pcgemm_.c',
  'pchemm_.c',
  'pcher2k_.c',
  'pcherk_.c',
  'pcsymm_.c',
  'pcsyr2k_.c',
  'pcsyrk_.c',
  'pctradd_.c',
  'pctranc_.c',
  'pctranu_.c',
  'pctrmm_.c',
  'pctrsm_.c',
)

pdblas3 = files(
  'pdgeadd_.c',
  'pdgemm_.c',
  'pdsymm_.c',
  'pdsyr2k_.c',
  'pdsyrk_.c',
  'pdtradd_.c',
  'pdtran_.c',
  'pdtrmm_.c',
  'pdtrsm_.c',
)

pzblas3 = files(
  'pzgeadd_.c',
  'pzgemm_.c',
  'pzhemm_.c',
  'pzher2k_.c',
  'pzherk_.c',
  'pzsymm_.c',
  'pzsyr2k_.c',
  'pzsyrk_.c',
  'pztradd_.c',
  'pztranc_.c',
  'pztranu_.c',
  'pztrmm_.c',
  'pztrsm_.c',
)

pblas_srcs = [
  piblas1,
  psblas1,
  pcblas1,
  pdblas1,
  pzblas1,
  psblas2,
  pcblas2,
  pdblas2,
  pzblas2,
  psblas3,
  pcblas3,
  pdblas3,
  pzblas3,
]
pblas_f_srcs = appblas
