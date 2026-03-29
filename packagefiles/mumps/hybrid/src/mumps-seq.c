#include "cmumps_c.h"
#include "dmumps_c.h"
#include "smumps_c.h"
#include "zmumps_c.h"

#include "mumps-hybrid.h"

void cmumps_seq(CMUMPS_STRUC_C* struc) {
  cmumps_c(struc);
}
void dmumps_seq(DMUMPS_STRUC_C* struc) {
  dmumps_c(struc);
}
void smumps_seq(SMUMPS_STRUC_C* struc) {
  smumps_c(struc);
}
void zmumps_seq(ZMUMPS_STRUC_C* struc) {
  zmumps_c(struc);
}
