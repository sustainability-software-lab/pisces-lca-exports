# AgileLCA: Findings

AgileLCA is a web-based LCA tool used at Lawrence Berkeley National Lab.

---

## Status

Integration is already live in PISCES (as of June 2026). PISCES generates a
y-vector from SFF data and passes it to the AgileLCA API.

Use this file to document gaps, edge cases, and anything that came up during testing.

---

## What AgileLCA needs: the y-vector

A y-vector is a list of every purchasable input a bioprocess uses, paired with how
much of each is needed per unit of product.

```json
[
  { "product_id": "agilelca-glucose-001", "quantity": 1200.0, "unit": "kg/h" },
  { "product_id": "agilelca-electricity-002", "quantity": 5000.0, "unit": "kWh/h" }
]
```

Key fields:
- `product_id`: AgileLCA's internal ID for the input material. Must match exactly.
- `quantity`: How much of this input is used.
- `unit`: Unit of the quantity (kg/h, kWh/h, MJ/h, etc.).

---

## Mapping from SFF

| AgileLCA field | Source in SFF |
|---|---|
| `product_id` | Matched from `streams[].composition[].component_name` via a hardcoded name map + fuzzy fallback |
| `quantity` | `streams[].stream_properties.total_mass_flow.value` x `composition[].mol_fraction` (approx per-component flow) |
| `unit` | Assumed kg/h from `total_mass_flow.units` |

The hardcoded name map lives in the PISCES frontend. It should be migrated here.

---

## Known gaps

- **Mass flow missing in PDF-imported SFFs**: `total_mass_flow` is null for most
  flowsheets imported from PDFs. The y-vector quantity will be unknown for those.
- **Chemical name mismatches**: Some PISCES component names do not match any AgileLCA
  product ID even with fuzzy matching. These show up as unmatched entries.
- **Energy inputs**: PISCES SFF does not have utility consumption fields populated
  for most flowsheets yet. Steam and electricity inputs to the process are missing.

---

## Open questions

- What is the authoritative list of AgileLCA product IDs? Is there an API endpoint
  to fetch it?
- How does AgileLCA handle multi-product flowsheets (allocation)?

---

## References

- AgileLCA main interface: ask Tyler for the internal URL
- y-vector API: ask Tyler for the endpoint docs
- Related PISCES frontend code: `lib/lca/agilelca.ts` (approximately -- confirm with Tyler)
