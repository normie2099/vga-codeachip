"""Multi-objective optimisation over the design space.

Owns: the pymoo NSGA-II problem definition, minimising (P, Vn_rms) subject
to Av/f_-3dB/PM/area constraints, evaluated from lut.py's interpolators
(never from SPICE directly). Writes cache/pareto_results.json.

Phase 4 of the plan. Not implemented yet.
"""
