"""
pygreet.py

Converts PISCES SFF data to PyGREET-compatible input.

Status: placeholder. PyGREET (Argonne Python GREET) was just released in beta
as of June 2026. The input format needs to be researched before this module
can be implemented.

References:
- Paper: doi:10.1016/j.envsoft.2026.107072
- Beta download: https://anl.app.box.com/s/zz58d5elv2jl7e4wt722spqu6w3l26y1
- User guide: https://argonne-national-laboratory-aet.github.io/PyGREET-user-manual/

TODO:
1. Download the PyGREET beta and install it.
2. Find the API for defining a new bioprocess pathway.
3. Determine what input fields are required.
4. Document findings in research/pygreet/FINDINGS.md.
5. Implement this function.
"""

from typing import Any
from pisces_lca_exports.sff_reader import read_sff


def sff_to_pygreet(sff: dict[str, Any]) -> dict:
    """
    Convert an SFF JSON dict to PyGREET pathway inputs.

    NOT YET IMPLEMENTED. Returns a stub dict with the data extracted from SFF
    so you can see what is available to work with.

    Replace this implementation once the PyGREET API is understood.
    """
    exchanges_data = read_sff(sff)

    return {
        "_status": "not_implemented",
        "_note": (
            "PyGREET input format is not yet researched. "
            "See research/pygreet/FINDINGS.md."
        ),
        "process_title": exchanges_data.process_title,
        "simulator": exchanges_data.simulator_name,
        "inputs": [
            {
                "stream_id": ex.stream_id,
                "components": ex.components,
                "mass_flow_kg_h": ex.mass_flow_kg_h,
            }
            for ex in exchanges_data.inputs
        ],
        "outputs": [
            {
                "stream_id": ex.stream_id,
                "components": ex.components,
                "mass_flow_kg_h": ex.mass_flow_kg_h,
            }
            for ex in exchanges_data.outputs
        ],
    }
