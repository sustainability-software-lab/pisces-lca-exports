# Brightway: Findings

Brightway is a Python framework for life cycle assessment. It is widely used in
academic LCA research.

- GitHub: https://github.com/brightway-lca/brightway2
- Docs: https://docs.brightway.dev/
- Key paper: Mutel (2017), JOSS, doi:10.21105/joss.00236

---

## Status

Not yet implemented. This file is where you document what you learn about Brightway's
data model before writing `src/pisces_lca_exports/brightway.py`.

---

## What Brightway needs

Brightway organizes data as **Activities** connected by **Exchanges**.

An Activity is a process (e.g. "ethanol production"). An Exchange connects two
activities (e.g. "glucose input to ethanol production at rate 1.2 kg/kg ethanol").

To describe a PISCES flowsheet in Brightway, you need:

1. One Activity for the overall process.
2. One Exchange per input stream (type: `technosphere` or `biosphere`).
3. One Exchange for the main product output (type: `production`).

Minimal Activity structure (Brightway 2 format):

```python
{
    "name": "Ethanol production from corn stover",
    "unit": "kg",          # unit of the functional unit
    "location": "US",
    "exchanges": [
        {
            "input": ("ecoinvent", "some-uuid"),  # upstream process
            "amount": 1.2,
            "unit": "kg",
            "type": "technosphere",               # input from another process
        },
        {
            "input": ("my_db", "this-activity-uuid"),
            "amount": 1.0,
            "unit": "kg",
            "type": "production",                 # this activity's output
        },
    ]
}
```

---

## What to fill in here

As you research Brightway, answer these questions in this file:

1. What is the minimal set of fields needed for a valid Activity?
2. What databases does Brightway work with (ecoinvent, USLCI, etc.)?
3. How do you import an Activity from a dict (what API call)?
4. How do you match a chemical name from PISCES to an existing Brightway Activity?
5. What fields in SFF map directly to Brightway fields? What gaps are there?

---

## Open questions

- Does Brightway have a standard PISCES or bioprocess database anyone has already built?
- Is Brightway 2 or Brightway 25 (the newer version) the right target?

---

## References

- Brightway 2 docs: https://docs.brightway.dev/
- Brightway GitHub: https://github.com/brightway-lca/brightway2
- Tutorial notebooks: https://github.com/brightway-lca/brightway2/tree/master/notebooks
