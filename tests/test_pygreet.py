"""Tests for pygreet.py.

PyGREET export is not yet implemented. These tests verify the placeholder
behavior and will be updated when the real implementation is added.
"""

from pisces_lca_exports.pygreet import sff_to_pygreet


def test_returns_dict(minimal_sff):
    result = sff_to_pygreet(minimal_sff)
    assert isinstance(result, dict)


def test_status_is_not_implemented(minimal_sff):
    result = sff_to_pygreet(minimal_sff)
    assert result["_status"] == "not_implemented"


def test_process_title_present(minimal_sff):
    result = sff_to_pygreet(minimal_sff)
    assert result["process_title"] == "Test Bioethanol Process"


def test_inputs_and_outputs_present(minimal_sff):
    result = sff_to_pygreet(minimal_sff)
    assert len(result["inputs"]) == 1
    assert len(result["outputs"]) == 1
