# Open LCA Databases: Findings

LCA tools need background databases to get upstream emissions and energy data for
each input material. This file tracks which databases are publicly available,
what they cover, and which LCA tools they work with.

---

## Why this matters

When a PISCES flowsheet says "1200 kg/h of Glucose enters the process," an LCA
tool needs to know the environmental impact of producing that glucose. That
background data comes from an LCA database.

The choice of database determines:
- Which chemicals can be resolved (if a chemical is not in the database, the LCA
  has a gap)
- The geographic scope of the results (US-specific vs global)
- Whether the tool is free to use for commercial work

---

## Known public databases

| Database | Coverage | Format | License | Notes |
|---|---|---|---|---|
| USLCI | US processes | JSON-LD, OpenLCA format | Public domain | National Renewable Energy Lab. Good for US bioprocesses. |
| ecoinvent | Global, ~18,000 processes | Paid, multiple formats | Commercial | Gold standard but not free. LBL may have a license. |
| ELCD | European processes | JSON-LD | Free | European Commission. Less relevant for US bioprocesses. |
| Agri-footprint | Agricultural inputs | OpenLCA, Brightway | Commercial | Covers feedstocks like corn, sugarcane, algae. |
| ProBas | German processes | Various | Free | German Environment Agency. |

---

## Chemical name matching

A recurring problem: PISCES stores chemical names as strings (e.g. "Glucose",
"Sodium Hydroxide", "CO2"). LCA databases use their own identifiers.
Matching between them requires either:
1. A hardcoded map of PISCES names to database IDs
2. CAS number matching (if PISCES stores CAS numbers)
3. Fuzzy string matching as a fallback

Document any successful or failed matches here as they come up.

---

## Open questions

- Does LBL have an ecoinvent license that Aarav can use?
- Is there a standard mapping between PISCES compound names and USLCI flow UUIDs?
- Are there bioprocess-specific databases (bioethanol, biodiesel, fermentation inputs)
  that go beyond what USLCI covers?

---

## References

- USLCI: https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public
- ecoinvent: https://ecoinvent.org/
- ELCD: https://eplca.jrc.ec.europa.eu/ELCD3/
- LCA Commons (hosts USLCI and others): https://www.lcacommons.gov/
