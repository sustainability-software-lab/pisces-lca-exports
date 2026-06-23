"""Tests for brightway.py."""

from pisces_lca_exports.brightway import sff_to_brightway


def test_returns_dict(minimal_sff):
    result = sff_to_brightway(minimal_sff)
    assert isinstance(result, dict)


def test_name_set(minimal_sff):
    result = sff_to_brightway(minimal_sff)
    assert result["name"] == "Test Bioethanol Process"


def test_exchanges_present(minimal_sff):
    result = sff_to_brightway(minimal_sff)
    assert len(result["exchanges"]) > 0


def test_has_at_least_one_production_exchange(minimal_sff):
    result = sff_to_brightway(minimal_sff)
    production = [e for e in result["exchanges"] if e["type"] == "production"]
    assert len(production) > 0


def test_technosphere_exchanges_from_inputs(minimal_sff):
    result = sff_to_brightway(minimal_sff)
    technosphere = [e for e in result["exchanges"] if e["type"] == "technosphere"]
    names = [e["_pisces_component_name"] for e in technosphere]
    assert "Glucose" in names


def test_sparse_sff_does_not_crash(sparse_sff):
    result = sff_to_brightway(sparse_sff)
    assert isinstance(result, dict)
    # mass flow missing -> amount should be None for sparse imports
    assert any(e["amount"] is None for e in result["exchanges"])
