"""Shared pytest fixtures."""

import pytest


MINIMAL_SFF = {
    "metadata": {
        "sff_version": "0.0.3",
        "process_title": "Test Bioethanol Process",
        "process_simulator": {"name": "BioSTEAM", "version": "2.x"},
        "feedstocks": [],
        "products": [],
    },
    "units": [
        {
            "id": "RX-01",
            "unit_type": "Reactor",
            "design_input_specs": {},
            "design_results": {},
            "installed_costs": {},
            "purchase_costs": {},
            "utility_consumption_results": {},
            "utility_production_results": {},
            "reactions": [],
        }
    ],
    "streams": [
        {
            "id": "S-01",
            "source_unit_id": "None",
            "sink_unit_id": "RX-01",
            "stream_type": "feed",
            "stream_properties": {
                "total_mass_flow": {"value": 1000.0, "units": "kg/h"},
                "temperature": {"value": 298.15, "units": "K"},
                "pressure": {"value": 101325.0, "units": "Pa"},
                "total_molar_flow": {"value": 31.25, "units": "kmol/h"},
                "total_volumetric_flow": {"value": 1.265, "units": "m3/h"},
            },
            "composition": [
                {"component_name": "Glucose", "mol_fraction": 0.90, "phase": "l"},
                {"component_name": "Water", "mol_fraction": 0.10, "phase": "l"},
            ],
        },
        {
            "id": "S-02",
            "source_unit_id": "RX-01",
            "sink_unit_id": "None",
            "stream_type": "product",
            "stream_properties": {
                "total_mass_flow": {"value": 460.0, "units": "kg/h"},
                "temperature": {"value": 310.0, "units": "K"},
                "pressure": {"value": 101325.0, "units": "Pa"},
                "total_molar_flow": {"value": 10.0, "units": "kmol/h"},
                "total_volumetric_flow": {"value": 0.58, "units": "m3/h"},
            },
            "composition": [
                {"component_name": "Ethanol", "mol_fraction": 0.95, "phase": "l"},
                {"component_name": "Water", "mol_fraction": 0.05, "phase": "l"},
            ],
        },
    ],
}

# SFF with no mass flow data (PDF-imported style)
SPARSE_SFF = {
    "metadata": {
        "sff_version": "0.0.3",
        "process_title": "Sparse PDF-imported Process",
        "process_simulator": {"name": "unknown"},
        "feedstocks": [],
        "products": [],
    },
    "units": [],
    "streams": [
        {
            "id": "S-01",
            "source_unit_id": "None",
            "sink_unit_id": "None",
            "stream_type": "feed",
            "stream_properties": {},
            "composition": [
                {"component_name": "Glucose", "mol_fraction": 1.0, "phase": "l"},
            ],
        },
    ],
}


@pytest.fixture()
def minimal_sff():
    return MINIMAL_SFF


@pytest.fixture()
def sparse_sff():
    return SPARSE_SFF
