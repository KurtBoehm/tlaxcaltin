# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# subdir('LAPACK')

atools = files(
  'SL_init.f',
  'chk1mat.f',
  'desc_convert.f',
  'descinit.f',
  'descset.f',
  'iceil.f',
  'ilacpy.f',
  'ilcm.f',
  'indxg2l.f',
  'indxg2p.f',
  'indxl2g.f',
  'infog1l.f',
  'infog2l.f',
  'npreroc.f',
  'numroc.f',
  'pchkxmat.f',
  'sltimer.f',
)

itools = files(
  'pichekpad.f',
  'picol2row.f',
  'pielget.f',
  'pielset.f',
  'pielset2.f',
  'pifillpad.f',
  'pilaprnt.f',
  'pirow2col.f',
  'pitreecomb.f',
)

stools = files(
  'dsasum.f',
  'dsnrm2.f',
  'pschekpad.f',
  'pscol2row.f',
  'pselget.f',
  'pselset.f',
  'pselset2.f',
  'psfillpad.f',
  'pslaprnt.f',
  'pslaread.f',
  'pslawrite.f',
  'psmatadd.f',
  'psrow2col.f',
  'pstreecomb.f',
  'slatcpy.f',
  'smatadd.f',
  'ssdot.f',
)

dtools = files(
  'dddot.f',
  'dlatcpy.f',
  'dmatadd.f',
  'pdchekpad.f',
  'pdcol2row.f',
  'pdelget.f',
  'pdelset.f',
  'pdelset2.f',
  'pdfillpad.f',
  'pdlaprnt.f',
  'pdlaread.f',
  'pdlawrite.f',
  'pdmatadd.f',
  'pdrow2col.f',
  'pdtreecomb.f',
)

ctools = files(
  'ccdotc.f',
  'ccdotu.f',
  'clatcpy.f',
  'cmatadd.f',
  'dscasum.f',
  'dscnrm2.f',
  'pcchekpad.f',
  'pccol2row.f',
  'pcelget.f',
  'pcelset.f',
  'pcelset2.f',
  'pcfillpad.f',
  'pclaprnt.f',
  'pclaread.f',
  'pclawrite.f',
  'pcmatadd.f',
  'pcrow2col.f',
  'pctreecomb.f',
)

ztools = files(
  'pzchekpad.f',
  'pzcol2row.f',
  'pzelget.f',
  'pzelset.f',
  'pzelset2.f',
  'pzfillpad.f',
  'pzlaprnt.f',
  'pzlaread.f',
  'pzlawrite.f',
  'pzmatadd.f',
  'pzrow2col.f',
  'pztreecomb.f',
  'zlatcpy.f',
  'zmatadd.f',
  'zzdotc.f',
  'zzdotu.f',
)

tools_srcs = atools + itools + stools + dtools + ctools + ztools

tools_c_srcs = files('SL_gridreshape.c', 'reshape.c')
