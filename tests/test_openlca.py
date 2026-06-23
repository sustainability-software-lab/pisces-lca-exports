"""Tests for openlca.py."""

from pisces_lca_exports.openlca import sff_to_openlca


def test_returns_dict(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    assert isinstance(result, dict)


def test_type_is_process(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    assert result["@type"] == "Process"


def test_name_set(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    assert result["name"] == "Test Bioethanol Process"


def test_has_exchanges(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    assert len(result["exchanges"]) > 0


def test_exactly_one_quantitative_reference(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    qr = [e for e in result["exchanges"] if e.get("quantitativeReference")]
    assert len(qr) == 1


def test_inputs_have_input_true(minimal_sff):
    result = sff_to_openlca(minimal_sff)
    inputs = [e for e in result["exchanges"] if e["input"] is True]
    assert len(inputs) > 0


def test_sparse_sff_does_not_crash(sparse_sff):
    result = sff_to_openlca(sparse_sff)
    assert result["@type"] == "Process"
