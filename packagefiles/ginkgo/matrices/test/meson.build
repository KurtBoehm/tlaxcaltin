# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

foreach n : [
  '1138_bus_mc64_result',
  '1138_bus_shuffled',
  '1138_bus',
  'ani1_amd_chol',
  'ani1_amd_lu',
  'ani1_amd',
  'ani1_chol',
  'ani1_lu',
  'ani1_nonsymm_lu',
  'ani1_nonsymm',
  'ani1',
  'ani4_amd_chol',
  'ani4_amd_lu',
  'ani4_amd',
  'ani4_chol',
  'ani4_lu',
  'ani4',
  'isai_a_excess_rhs',
  'isai_a_excess',
  'isai_a_inv_partial',
  'isai_a_inv',
  'isai_a',
  'isai_l_excess_rhs',
  'isai_l_excess',
  'isai_l_inv_partial',
  'isai_l_inv',
  'isai_l',
  'isai_spd_excess_rhs',
  'isai_spd_excess',
  'isai_spd_inv_partial',
  'isai_spd_inv',
  'isai_spd',
  'isai_u_excess_rhs',
  'isai_u_excess',
  'isai_u_inv_partial',
  'isai_u_inv',
  'isai_u',
  'nontrivial_mc64_example',
  'nontrivial_mc64_result',
]
  configure_file(copy: true, input: f'@n@.mtx', output: f'@n@.mtx')
endforeach
