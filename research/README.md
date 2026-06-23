# research/

Each subfolder here covers one LCA tool. You add notes to the `FINDINGS.md` file
inside the folder as you learn things about that tool.

The goal is to answer four questions for each tool:

1. **What input format does it need?** (What does the data structure look like?)
2. **What fields are required vs optional?**
3. **How do those fields map to what is already in an SFF file?**
4. **What is missing?** (What SFF fields would need to be added, estimated, or looked up
   to fill the gaps?)

You do not need to write code to fill in a FINDINGS.md. Notes, copied examples,
links to relevant docs, and questions you still have open are all useful.

Once a FINDINGS.md is detailed enough that someone could write a converter from it,
the corresponding module in `src/pisces_lca_exports/` can be implemented.

---

## Folders

| Folder | Tool | Priority |
|---|---|---|
| `agilelca/` | AgileLCA (web LCA tool at LBL) | Integration already live in PISCES. Document gaps. |
| `brightway/` | Brightway (Python LCA framework) | High. Widely used in research. |
| `openlca/` | OpenLCA (free desktop LCA) | Medium. Broad user base, ecoinvent-compatible. |
| `pygreet/` | PyGREET (Argonne Python GREET) | High. Just published (June 2025). Relevant to US bioprocess LCA. |
| `open_databases/` | LCA databases (ecoinvent, USLCI, etc.) | Ongoing. Needed for all of the above to resolve chemical identities. |

---

## How to add a finding

1. Open the `FINDINGS.md` in the relevant subfolder.
2. Add what you found under the appropriate heading.
3. Link to the source (doc page, code file, paper DOI) whenever possible.
4. If you find something that changes the implementation plan, leave a note under
   **Open questions** so it can be discussed.

You can also add files (e.g. a downloaded example output, a copied JSON schema) to
the subfolder. Keep large binary files out of the repo.
