"""Tests for sff_reader.py."""

import pytest
from pisces_lca_exports.sff_reader import read_sff


def test_process_title(minimal_sff):
    result = read_sff(minimal_sff)
    assert result.process_title == "Test Bioethanol Process"


def test_inputs_extracted(minimal_sff):
    result = read_sff(minimal_sff)
    assert len(result.inputs) == 1
    assert result.inputs[0].stream_id == "S-01"
    assert result.inputs[0].stream_type == "feed"


def test_outputs_extracted(minimal_sff):
    result = read_sff(minimal_sff)
    assert len(result.outputs) == 1
    assert result.outputs[0].stream_id == "S-02"
    assert result.outputs[0].stream_type == "product"


def test_internal_streams_excluded(minimal_sff):
    sff = dict(minimal_sff)
    sff["streams"] = list(minimal_sff["streams"]) + [
        {
            "id": "S-99",
            "source_unit_id": "RX-01",
            "sink_unit_id": "RX-01",
            "stream_type": "internal",
            "stream_properties": {},
            "composition": [],
        }
    ]
    result = read_sff(sff)
    ids = [ex.stream_id for ex in result.inputs + result.outputs]
    assert "S-99" not in ids


def test_mass_flow_populated(minimal_sff):
    result = read_sff(minimal_sff)
    assert result.inputs[0].mass_flow_kg_h == pytest.approx(1000.0)


def test_mass_flow_none_when_missing(sparse_sff):
    result = read_sff(sparse_sff)
    assert result.inputs[0].mass_flow_kg_h is None


def test_composition_passed_through(minimal_sff):
    result = read_sff(minimal_sff)
    names = [c["component_name"] for c in result.inputs[0].components]
    assert "Glucose" in names
    assert "Water" in names
