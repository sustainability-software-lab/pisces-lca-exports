"""
sff_reader.py

Reads an SFF JSON dict and extracts the input/output streams in a form
that each LCA exporter can work with.

All LCA exporters call read_sff() first, then use the SffExchanges result.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LcaExchange:
    """One material exchange: a stream entering or leaving the process."""

    stream_id: str
    stream_type: str                # "feed", "product", "waste", "internal"
    components: list[dict]          # [{component_name, mol_fraction, phase}]
    mass_flow_kg_h: float | None    # None if not present in SFF
    temperature_k: float | None
    pressure_pa: float | None


@dataclass
class SffExchanges:
    """The inputs and outputs of a PISCES flowsheet, extracted for LCA use."""

    process_title: str
    sff_version: str
    simulator_name: str

    inputs: list[LcaExchange] = field(default_factory=list)
    outputs: list[LcaExchange] = field(default_factory=list)

    # Streams marked as products in metadata (human-reviewed)
    designated_products: list[str] = field(default_factory=list)


def read_sff(sff: dict[str, Any]) -> SffExchanges:
    """
    Extract feed and product exchanges from an SFF JSON dict.

    Returns SffExchanges with inputs (stream_type == "feed") and
    outputs (stream_type == "product" or "waste").

    Mass flow is populated when total_mass_flow is present in stream_properties.
    Many PDF-imported flowsheets do not have mass flow data; in those cases
    mass_flow_kg_h is None and the LCA exporter must handle the missing quantity.
    """
    metadata = sff.get("metadata", {})
    streams = sff.get("streams", [])

    exchanges = SffExchanges(
        process_title=metadata.get("process_title") or "Unknown process",
        sff_version=metadata.get("sff_version", "unknown"),
        simulator_name=(metadata.get("process_simulator") or {}).get("name", "unknown"),
        designated_products=[
            p.get("stream_id") for p in (metadata.get("products") or [])
            if p.get("stream_id")
        ],
    )

    for stream in streams:
        stream_type = stream.get("stream_type", "internal")
        if stream_type == "internal":
            continue

        props = stream.get("stream_properties") or {}
        mass_flow_entry = props.get("total_mass_flow") or {}
        mass_flow = mass_flow_entry.get("value")

        temp_entry = props.get("temperature") or {}
        pres_entry = props.get("pressure") or {}

        exchange = LcaExchange(
            stream_id=stream.get("id", ""),
            stream_type=stream_type,
            components=stream.get("composition") or [],
            mass_flow_kg_h=float(mass_flow) if mass_flow is not None else None,
            temperature_k=float(temp_entry["value"]) if temp_entry.get("value") is not None else None,
            pressure_pa=float(pres_entry["value"]) if pres_entry.get("value") is not None else None,
        )

        if stream_type == "feed":
            exchanges.inputs.append(exchange)
        else:
            exchanges.outputs.append(exchange)

    return exchanges
