# SFF Field Mapping for LCA Exports

This document explains which fields in an SFF JSON file are used for LCA exports
and what those fields mean.

---

## SFF structure overview

An SFF file has three top-level sections:

```json
{
  "metadata": { ... },
  "units": [ ... ],
  "streams": [ ... ]
}
```

For LCA exports, `metadata` and `streams` matter. `units` (the equipment list) is not
used for LCA calculations.

---

## Fields used in LCA exports

### From metadata

| Field | Type | What it means | LCA use |
|---|---|---|---|
| `process_title` | string | Name of the bioprocess | Used as the Activity/Process name in the target tool |
| `sff_version` | string | Schema version | Recorded in export comments for traceability |
| `process_simulator.name` | string | DWSIM, BioSTEAM, SuperPro, etc. | Recorded in export comments |
| `products` | array | Which streams are the main products (human-reviewed) | Sets the functional unit |

### From streams

| Field | Type | What it means | LCA use |
|---|---|---|---|
| `stream_type` | string | `"feed"`, `"product"`, `"waste"`, `"internal"` | Determines if the stream is an LCA input, output, or skipped |
| `stream_properties.total_mass_flow.value` | number | kg/h total mass flow | Sets the exchange amount |
| `stream_properties.total_mass_flow.units` | string | Always `"kg/h"` in current SFFs | Confirms unit for the exchange |
| `composition[].component_name` | string | Chemical name (e.g. "Glucose", "Ethanol") | Must be matched to the LCA database |
| `composition[].mol_fraction` | number | Fraction of the stream that is this chemical (molar basis) | Combined with mass_flow to estimate per-chemical quantities |

---

## How per-chemical quantities are estimated

SFF stores `total_mass_flow` for the whole stream and `mol_fraction` per component.
To get a per-chemical mass flow, the code currently multiplies:

```
per_component_flow ≈ total_mass_flow * mol_fraction
```

This is an approximation because `mol_fraction` is molar, not mass-based.
A correct calculation needs the molecular weight of each component.
That is a known gap -- see open issues.

---

## When mass flow is missing

PDF-imported SFFs often have `stream_properties` as `{}` or missing `total_mass_flow`.
In those cases `mass_flow_kg_h` is `None` and the LCA exchange quantity is unknown.

The exporters return `None` for the amount rather than inventing a number.
The PISCES import UI warns the user when this happens.

---

## What is NOT used

| Field | Why not used |
|---|---|
| `units[]` | Equipment list. Not needed for LCA (LCA cares about inputs/outputs, not what equipment processes them) |
| `stream_properties.temperature` | Not a standard LCA exchange field |
| `stream_properties.pressure` | Same |
| `design_input_specs` | Equipment design parameters, not LCA data |
| `design_results` | Equipment simulation outputs, not LCA data |

---

## Open gaps

1. **Mol fraction vs mass fraction**: per-component quantities need molecular weights
   to be accurate. Add MW lookup to `sff_reader.py` when a source is identified.
2. **Energy inputs**: steam, electricity, cooling water are not in SFF composition.
   They would be in `utility_consumption_results` but that field is empty for most
   current SFFs. Required for a complete LCA.
3. **Chemical name matching**: PISCES component names (free text) must match to
   LCA database identifiers. The matching strategy is different for each tool.
   See each tool's FINDINGS.md in `research/`.
