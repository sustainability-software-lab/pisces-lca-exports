# pisces-lca-exports

Export PISCES flowsheet data to formats that other LCA tools can read.

---

## What this repo is for

Project PISCES stores bioprocess flowsheets in SFF (Standard Flowsheet Format) JSON.
Other LCA tools like Brightway, OpenLCA, and PyGREET cannot read SFF directly.
This package converts SFF data into the input format each tool expects.

The repo has two parts:

1. **`research/`** -- One folder per LCA tool. This is where you document what you learn
   about each tool's data format, what inputs it needs, and where those inputs
   can come from in an SFF file. There is a template in each folder to guide what
   to write.

2. **`src/pisces_lca_exports/`** -- The Python package. One module per LCA tool.
   Each module reads an SFF JSON dict and returns the data structure that tool needs.

The research comes first. Fill in `research/<tool>/FINDINGS.md` before writing code
for that tool. The findings tell you what the code needs to produce.

---

## LCA tools we are targeting

| Tool | What it is | Status |
|---|---|---|
| Brightway | Python LCA framework. Widely used in research. | Scaffold ready. Research the exchange format and chemical matching before completing. |
| OpenLCA | Free desktop LCA software. Imports JSON-LD. | Scaffold ready. Research the JSON-LD schema and Flow UUID matching before completing. |
| PyGREET | Argonne Python GREET (just released June 2026). Computes carbon intensity for US bioprocesses. | Placeholder only. Download the beta and document the input API first. |

> **AgileLCA**: Integration already ships in the PISCES frontend. This repo does not cover it.
> If you find gaps in the AgileLCA integration while testing, file an issue in the
> [PISCES frontend repo](https://github.com/sustainability-software-lab/project-pisces-frontend).

---

## Where the data comes from in SFF

An SFF file has three sections: `metadata`, `units`, and `streams`.

For LCA exports, the relevant fields are:

| SFF field | What it represents | LCA use |
|---|---|---|
| `streams[].stream_type` | `"feed"` = enters the process; `"product"` = leaves | Identifies what is an input and what is an output |
| `streams[].stream_properties.total_mass_flow.value` | kg/h of material in the stream | Sets the quantity in the LCA exchange |
| `streams[].composition[].component_name` | Chemical name of each component | Maps to the LCA database substance |
| `streams[].composition[].mol_fraction` | Fraction of the stream that is this chemical | Combined with mass flow to get per-chemical quantities |
| `metadata.products` | Which streams the flowsheet author marked as products | Sets the functional unit |

Mass flow data is present in most SuperPro and BioSTEAM exports. It is sparse in
PDF-imported flowsheets. When mass flow is missing, the LCA export will note that
the quantity is unknown rather than inventing a number.

See `docs/SFF_FIELD_MAPPING.md` for the full mapping.

---

## Project structure

```
pisces-lca-exports/
├── src/
│   └── pisces_lca_exports/
│       ├── __init__.py            # Package public API
│       ├── sff_reader.py          # Reads SFF JSON and extracts feed/product streams
│       ├── agilelca.py            # Builds y-vectors for AgileLCA
│       ├── brightway.py           # Builds Activity + Exchange dicts for Brightway
│       ├── openlca.py             # Builds JSON-LD Process objects for OpenLCA
│       └── pygreet.py             # Builds DataFrames for PyGREET
├── tests/
│   ├── conftest.py                # Shared fixtures (sample SFF JSONs)
│   ├── test_sff_reader.py
│   ├── test_agilelca.py
│   ├── test_brightway.py
│   ├── test_openlca.py
│   └── test_pygreet.py
├── research/
│   ├── README.md                  # How to use the research folder
│   ├── agilelca/
│   │   └── FINDINGS.md            # Document what you learn about AgileLCA's format
│   ├── brightway/
│   │   └── FINDINGS.md
│   ├── openlca/
│   │   └── FINDINGS.md
│   ├── pygreet/
│   │   └── FINDINGS.md
│   └── open_databases/
│       └── FINDINGS.md            # LCA databases that are publicly available
├── docs/
│   ├── SFF_FIELD_MAPPING.md       # How SFF fields map to LCA concepts
│   └── DEVELOPMENT.md             # How to set up and run tests locally
├── pyproject.toml
├── Makefile
└── .gitignore
```

---

## Quick start

```bash
git clone git@github.com:sustainability-software-lab/pisces-lca-exports.git
cd pisces-lca-exports

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Run tests
make test
```

### Convert an SFF file to an AgileLCA y-vector

```python
import json
from pisces_lca_exports import sff_to_agilelca

with open("flowsheet.json") as f:
    sff = json.load(f)

y_vector = sff_to_agilelca(sff)
print(y_vector)
# [
#   {"product_name": "Glucose", "quantity": 1200.0, "unit": "kg/h"},
#   {"product_name": "Ammonia", "quantity": 50.0, "unit": "kg/h"},
#   ...
# ]
```

---

## Related

- [Project PISCES frontend](https://github.com/sustainability-software-lab/project-pisces-frontend) -- main app
- [pisces-standard-flowsheet-format](https://github.com/sustainability-software-lab/pisces-standard-flowsheet-format) -- SFF schema
- [pisces-dwsim-importer](https://github.com/sustainability-software-lab/pisces-dwsim-importer) -- DWSIM to SFF converter
- Tracking issue: #2313 in the PISCES frontend repo
