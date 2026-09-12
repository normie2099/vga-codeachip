"""Device characterisation: sweep + parsing.

Owns: the ngspice .dc nested sweep over the char testbench (L, Vgs, Vds),
and parsing raw ngspice output into the normalised (Id/W, gm/Id, gds/Id,
Cgs/Id, Cgd/Id) table written to cache/lut_sky130.parquet.

Phase 2 of the plan. Not implemented yet.
"""
