"""
pisces-lca-exports

Converts PISCES SFF (Standard Flowsheet Format) JSON to formats
compatible with external LCA tools.

Supported targets:
- Brightway 2 / Brightway 25
- OpenLCA (JSON-LD)
- PyGREET (Argonne Python GREET)

AgileLCA integration already lives in the PISCES frontend. See:
https://github.com/sustainability-software-lab/project-pisces-frontend

Usage:
    from pisces_lca_exports import sff_to_brightway, sff_to_openlca, sff_to_pygreet
"""

from pisces_lca_exports.sff_reader import read_sff, SffExchanges
from pisces_lca_exports.brightway import sff_to_brightway
from pisces_lca_exports.openlca import sff_to_openlca
from pisces_lca_exports.pygreet import sff_to_pygreet

__version__ = "0.1.0"
__all__ = [
    "read_sff",
    "SffExchanges",
    "sff_to_brightway",
    "sff_to_openlca",
    "sff_to_pygreet",
]
