# Development Guide

How to set up, iterate, and test locally.

---

## Setup

```bash
git clone git@github.com:sustainability-software-lab/pisces-lca-exports.git
cd pisces-lca-exports

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e ".[dev]"

# Confirm it works
python -c "from pisces_lca_exports import sff_to_brightway; print('ok')"
```

---

## Running tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run tests for one tool only
pytest tests/test_brightway.py -v
```

---

## The research-first workflow

For any LCA tool that is not yet implemented:

1. Download the tool and install it.
2. Find a minimal working example in its docs.
3. Write down what the example data looks like in `research/<tool>/FINDINGS.md`.
4. Answer the four questions in the research/README.md template.
5. Write a failing test that describes what `sff_to_<tool>()` should return.
6. Implement the function until the test passes.

The existing scaffold functions (`sff_to_brightway`, `sff_to_openlca`, `sff_to_pygreet`)
already extract the right data from SFF. The main work is:
- Filling in the `input` field for each exchange (chemical name -> tool-specific ID)
- Confirming the output structure matches what the tool actually accepts

---

## Working with the SFF reader

`sff_reader.read_sff()` does the shared work of extracting feed and product streams
from any SFF file. All exporters call it first:

```python
from pisces_lca_exports.sff_reader import read_sff

with open("flowsheet.json") as f:
    import json
    sff = json.load(f)

exchanges = read_sff(sff)

print(f"Inputs: {len(exchanges.inputs)}")
print(f"Outputs: {len(exchanges.outputs)}")

for ex in exchanges.inputs:
    print(f"  {ex.stream_id}: {ex.mass_flow_kg_h} kg/h")
    for c in ex.components:
        print(f"    {c['component_name']}: {c['mol_fraction']}")
```

---

## Adding a new LCA tool

1. Add a new module: `src/pisces_lca_exports/<toolname>.py`
2. Add a `sff_to_<toolname>(sff: dict) -> <return_type>` function
3. Export it from `src/pisces_lca_exports/__init__.py`
4. Add tests to `tests/test_<toolname>.py`
5. Add a research folder: `research/<toolname>/FINDINGS.md`
6. Update the table in `README.md`

---

## Getting sample SFF files

Sample SFF files for testing are in the [pisces-standard-flowsheet-format](https://github.com/sustainability-software-lab/pisces-standard-flowsheet-format) repo and in the
[public SFF database](https://github.com/sustainability-software-lab/project-pisces-frontend/tree/main/public/sff-database/files)
in the main PISCES repo.

The `corn_ethanol.json` file in the PISCES repo is a good test case because it has
full mass flow data (BioSTEAM export).
