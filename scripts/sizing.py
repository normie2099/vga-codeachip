"""Inverse sizing: specification -> device geometry.

Owns: size_from_spec(spec, gm_id, L) implementing
    ID = 2*pi*C_L*f_u / (gm/ID)
    W  = ID / (ID/W)|_{gm/ID, L}
    Av = (gm/ID) / (gds/ID)_tot

Phase 3 of the plan. Not implemented yet.
"""
