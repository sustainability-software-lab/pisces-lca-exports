# PyGREET: Findings

PyGREET is Argonne National Laboratory's Python implementation of the GREET model
(Greenhouse gases, Regulated Emissions, and Energy use in Technologies).

- Published: Cheng et al. (2026), Environmental Modelling & Software
  doi: https://doi.org/10.1016/j.envsoft.2026.107072
- Beta download: https://anl.app.box.com/s/zz58d5elv2jl7e4wt722spqu6w3l26y1
- User guide: https://argonne-national-laboratory-aet.github.io/PyGREET-user-manual/

This is a newly released tool (June 2025 beta). It is the Python successor to the
Excel-based GREET model that Argonne has maintained for decades.

---

## Status

Not yet implemented. Download and install the beta to explore the API before writing
`src/pisces_lca_exports/pygreet.py`.

---

## Why PyGREET matters for PISCES

GREET is the standard tool for carbon intensity (CI) calculations for US bioprocess
and transportation fuels. Many industry partners and regulators use GREET outputs.
If PISCES can generate PyGREET-compatible inputs from an SFF flowsheet, users can
run CI calculations directly from their PISCES data.

---

## What to figure out

The user guide is the best starting point. Key questions to answer in this file:

1. What does PyGREET expect as input? (A DataFrame? A config dict? A CSV file?)
2. What are the required columns/fields for a bioprocess pathway?
3. What does "one pathway" mean in PyGREET terms? Does it map 1:1 to one SFF file?
4. What outputs does PyGREET produce? (GHG intensity in gCO2e/MJ? Per kg of product?)
5. Can you run PyGREET programmatically (import it as a Python module) or is it CLI-only?

---

## Initial notes from Slack (June 12, 2026)

From Corinne: "ANL finally got with the times and made a Python version of GREET."
The beta version was linked above. Worth downloading and trying a sample calculation
before building the integration.

---

## Open questions

- What chemical/energy input names does PyGREET recognize? Is there a fixed list?
- Does PyGREET have built-in process inventory data (like ecoinvent) or does it need
  the user to supply all quantities?
- Is there a contact at ANL for questions about the API?

---

## References

- Paper: doi:10.1016/j.envsoft.2026.107072
- Beta: https://anl.app.box.com/s/zz58d5elv2jl7e4wt722spqu6w3l26y1
- User guide: https://argonne-national-laboratory-aet.github.io/PyGREET-user-manual/
- Original GREET model: https://greet.anl.gov/
