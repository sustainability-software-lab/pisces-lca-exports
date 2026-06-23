# OpenLCA: Findings

OpenLCA is a free, open-source desktop LCA application.

- Website: https://www.openlca.org/
- GitHub: https://github.com/GreenDelta/openLCA-App
- Import format: JSON-LD (ecoinvent-compatible)

---

## Status

Not yet implemented. Document what you learn here before writing
`src/pisces_lca_exports/openlca.py`.

---

## What OpenLCA needs

OpenLCA uses a JSON-LD format for data import. A "process" in OpenLCA looks like:

```json
{
  "@type": "Process",
  "@id": "some-uuid",
  "name": "Ethanol production from corn stover",
  "processType": "UNIT_PROCESS",
  "category": { "@type": "Category", "name": "biomass processing" },
  "exchanges": [
    {
      "flow": { "@type": "Flow", "@id": "glucose-flow-uuid", "name": "Glucose" },
      "flowProperty": { "@type": "FlowProperty", "name": "Mass" },
      "unit": { "@type": "Unit", "name": "kg" },
      "amount": 1.2,
      "input": true
    },
    {
      "flow": { "@type": "Flow", "@id": "ethanol-flow-uuid", "name": "Ethanol" },
      "flowProperty": { "@type": "FlowProperty", "name": "Mass" },
      "unit": { "@type": "Unit", "name": "kg" },
      "amount": 1.0,
      "input": false,
      "quantitativeReference": true
    }
  ]
}
```

---

## What to fill in here

1. What is the exact JSON-LD schema for a Process and Exchange?
2. How do you import a JSON-LD file into OpenLCA (File > Import > JSON-LD)?
3. What UUIDs do Flow objects need? Are there shared UUIDs for common chemicals?
4. Does OpenLCA have an API or is it always file-based import?
5. What LCA databases work with OpenLCA (ecoinvent, USLCI, ELCD)?

---

## Open questions

- Is there a mapping from common chemical names to OpenLCA Flow UUIDs for USLCI?
- Can openLCA-Python (olca-ipc) be used for programmatic import?

---

## References

- OpenLCA JSON-LD format spec: https://greendelta.github.io/olca-schema/
- olca-ipc Python client: https://github.com/GreenDelta/olca-ipc.py
- USLCI database: https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public
