"""
brightway.py

Converts PISCES SFF data to a Brightway 2 Activity dict.

Status: scaffold. The output structure is correct but chemical name -> Brightway
Flow lookup is not yet implemented (returns the PISCES component name as a
placeholder). Fill in FINDINGS.md before completing this module.

Brightway docs: https://docs.brightway.dev/
"""

from typing import Any
from pisces_lca_exports.sff_reader import read_sff, SffExchanges, LcaExchange
import uuid


def sff_to_brightway(sff: dict[str, Any]) -> dict:
    """
    Convert an SFF JSON dict to a Brightway 2 Activity dict.

    The returned dict can be imported into a Brightway database using:
        db = bw2data.Database("my_db")
        db.write({"my_db": {("my_db", activity_id): result}})

    Returns a dict with keys: name, unit, location, exchanges.

    NOTE: chemical name matching to Brightway flows is not yet implemented.
    Each exchange will have a placeholder `_pisces_component_name` field
    instead of a resolved `input` (database, code) tuple.
    Research what matching approach to use and document it in
    research/brightway/FINDINGS.md.
    """
    exchanges_data = read_sff(sff)
    activity_id = str(uuid.uuid4())

    exchanges = []

    for ex in exchanges_data.inputs:
        for component in ex.components:
            amount = _component_mass_flow(ex, component)
            exchanges.append({
                "_pisces_component_name": component["component_name"],
                "amount": amount,
                "unit": "kg/h",
                "type": "technosphere",
                "input": None,  # TODO: resolve to (database, code) via name matching
                "_mass_flow_available": ex.mass_flow_kg_h is not None,
            })

    for ex in exchanges_data.outputs:
        for component in ex.components:
            amount = _component_mass_flow(ex, component)
            exchanges.append({
                "_pisces_component_name": component["component_name"],
                "amount": amount,
                "unit": "kg/h",
                "type": "production" if ex.stream_type == "product" else "technosphere",
                "input": None,  # TODO: resolve
                "_mass_flow_available": ex.mass_flow_kg_h is not None,
            })

    return {
        "@id": activity_id,
        "name": exchanges_data.process_title,
        "unit": "kg",
        "location": "US",
        "comment": f"Exported from PISCES. Simulator: {exchanges_data.simulator_name}. SFF version: {exchanges_data.sff_version}.",
        "exchanges": exchanges,
    }


def _component_mass_flow(exchange: LcaExchange, component: dict) -> float | None:
    """Estimate per-component mass flow from total flow + molar fraction.

    This is an approximation because molar fraction != mass fraction.
    A proper calculation needs molecular weights. Return None if total flow
    is missing.
    """
    if exchange.mass_flow_kg_h is None:
        return None
    return exchange.mass_flow_kg_h * component.get("mol_fraction", 0.0)
