"""
openlca.py

Converts PISCES SFF data to an OpenLCA JSON-LD Process object.

Status: scaffold. The JSON-LD structure is correct but Flow UUID lookup is not
yet implemented. Fill in research/openlca/FINDINGS.md before completing this.

OpenLCA JSON-LD schema: https://greendelta.github.io/olca-schema/
"""

from typing import Any
from pisces_lca_exports.sff_reader import read_sff, LcaExchange
import uuid


def sff_to_openlca(sff: dict[str, Any]) -> dict:
    """
    Convert an SFF JSON dict to an OpenLCA JSON-LD Process object.

    The returned dict can be saved to a .json file and imported into OpenLCA
    via File > Import > JSON-LD.

    NOTE: Flow UUIDs are generated as placeholder UUIDs because the mapping
    from PISCES component names to OpenLCA Flow objects is not yet implemented.
    See research/openlca/FINDINGS.md for what needs to be researched.
    """
    exchanges_data = read_sff(sff)
    process_id = str(uuid.uuid4())

    exchanges = []
    is_first_output = True

    for ex in exchanges_data.inputs:
        for component in ex.components:
            flow_uuid = str(uuid.uuid4())  # TODO: look up from USLCI or ecoinvent
            exchanges.append({
                "flow": {
                    "@type": "Flow",
                    "@id": flow_uuid,
                    "name": component["component_name"],
                    "_note": "UUID is a placeholder. Replace with real USLCI/ecoinvent flow UUID.",
                },
                "flowProperty": {"@type": "FlowProperty", "name": "Mass"},
                "unit": {"@type": "Unit", "name": "kg"},
                "amount": _component_mass_flow(ex, component),
                "input": True,
            })

    for ex in exchanges_data.outputs:
        for component in ex.components:
            flow_uuid = str(uuid.uuid4())
            entry = {
                "flow": {
                    "@type": "Flow",
                    "@id": flow_uuid,
                    "name": component["component_name"],
                    "_note": "UUID is a placeholder.",
                },
                "flowProperty": {"@type": "FlowProperty", "name": "Mass"},
                "unit": {"@type": "Unit", "name": "kg"},
                "amount": _component_mass_flow(ex, component),
                "input": False,
            }
            if is_first_output:
                entry["quantitativeReference"] = True
                is_first_output = False
            exchanges.append(entry)

    return {
        "@type": "Process",
        "@id": process_id,
        "name": exchanges_data.process_title,
        "processType": "UNIT_PROCESS",
        "exchanges": exchanges,
        "description": (
            f"Exported from PISCES. "
            f"Simulator: {exchanges_data.simulator_name}. "
            f"SFF version: {exchanges_data.sff_version}."
        ),
    }


def _component_mass_flow(exchange: LcaExchange, component: dict) -> float | None:
    if exchange.mass_flow_kg_h is None:
        return None
    return exchange.mass_flow_kg_h * component.get("mol_fraction", 0.0)
