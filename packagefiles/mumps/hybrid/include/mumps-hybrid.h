#ifndef MUMPS_HYBRID_H
#define MUMPS_HYBRID_H

// IWYU pragma: begin_exports
#include "mumps_c_types.h"
#include "cmumps_c.h"
#include "dmumps_c.h"
#include "smumps_c.h"
#include "zmumps_c.h"
// IWYU pragma: end_exports

#ifdef __cplusplus
extern "C" {
#endif

void cmumps_seq(CMUMPS_STRUC_C* struc);
void dmumps_seq(DMUMPS_STRUC_C* struc);
void smumps_seq(SMUMPS_STRUC_C* struc);
void zmumps_seq(ZMUMPS_STRUC_C* struc);

void cmumps_par(CMUMPS_STRUC_C* struc);
void dmumps_par(DMUMPS_STRUC_C* struc);
void smumps_par(SMUMPS_STRUC_C* struc);
void zmumps_par(ZMUMPS_STRUC_C* struc);

#ifdef __cplusplus
}
#endif

#endif // MUMPS_HYBRID_H
