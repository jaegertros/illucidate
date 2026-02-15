# Example Datasets

This folder contains example datasets for testing and demonstrating Illucidate.

**IMPORTANT:** All datasets must include proper attribution and licensing information.

---

## Available Datasets

### 1. Victor Nivo Example (E. coli O157:H7)
- **Folder:** `victor_nivo_ecoli_o157h7/`
- **Format:** Victor Nivo Excel export
- **Measurements:** OD600, OD560, OD450
- **Wells:** 96
- **Timepoints:** 60 (12 hours)
- **License:** [Your license here]
- **Citation:** [If published]

---

## Adding New Datasets

### Requirements

1. **You must own the data OR have explicit permission to share it**
2. **Choose an appropriate license:**
   - **CC0** (Public Domain) - No restrictions
   - **CC-BY 4.0** - Attribution required
   - **CC-BY-NC 4.0** - Non-commercial use only
   - **Custom** - Specify restrictions clearly

3. **Provide complete metadata:**
   - Experimental conditions
   - Instrument/settings
   - Date collected
   - Publication reference (if published)

### Dataset Folder Structure

```
dataset_name/
├── README.md                  # Required - Attribution and details
├── data.xlsx                  # Raw data file(s)
├── experimental_design.csv    # Well annotations (optional but recommended)
└── metadata.json              # Machine-readable metadata (optional)
```

### Dataset README Template

Copy this template into your dataset folder:

```markdown
# Dataset: [Short Descriptive Name]

## Attribution

**Source:** [Published paper / Unpublished / Personal communication]
**DOI:** [DOI if published, or "N/A"]
**Original Authors:** [Names]
**Data Provider:** [Who gave permission, if different from authors]
**Date Collected:** [YYYY-MM-DD or YYYY-MM]

## License

[CC0 / CC-BY 4.0 / CC-BY-NC 4.0 / Custom]

**Usage Terms:**
- ✅ [What's allowed - e.g., "Use for research and teaching"]
- ✅ [e.g., "Modify and redistribute"]
- ❌ [What's not allowed - e.g., "Commercial use prohibited"]

**Attribution Requirement:**
If you use this data in publications, cite:
```
[Full citation in your field's format]
```

## Experimental Details

**Organism:** [Species and strain]
**Phage:** [Phage name/type, if applicable]
**Detection Method:** [Bioluminescence / OD / Fluorescence / etc.]
**Reporter:** [e.g., "NanoLuc luciferase"]

**Instrument:** [Make and model]
**Settings:** 
- Temperature: [°C]
- Shaking: [Yes/No, speed if applicable]
- Wavelengths: [e.g., "OD600, OD560"]

**Plate Layout:**
- Total wells: [Number]
- Replicates per condition: [Number]
- Controls: [Describe]

**Duration:** [X hours, Y minute intervals]
**Total Timepoints:** [Number]

## Files

**data.xlsx** - Raw export from [instrument]
- Sheet 1: [Description]
- Sheet 2: [Description]

**experimental_design.csv** - Well annotations
- Columns: Well, [experimental variables...]

**[Any other files]** - [Description]

## Variables Tested

| Variable | Levels |
|----------|--------|
| Bacterial strain | [List] |
| Concentration | [List] |
| [Other variables] | [List] |

## Known Issues / Notes

- [Any quirks about the data]
- [Known outliers or failed wells]
- [Special considerations]

## Contact

**Questions about this dataset:** [Email or GitHub username]
**Original study:** [Link to publication or N/A]

---

**By using this data, you agree to:**
1. Cite the original source
2. Follow the license terms
3. Not misrepresent the data or its origin
```

---

## Example Attribution in Papers

### In Methods Section:

> "Example data were obtained from the Illucidate repository (https://github.com/[user]/illucidate/examples/data/[dataset]) and analyzed under [license]. Original data were collected by [authors] and published in [citation]."

### In Acknowledgments:

> "We thank [names] for making their data publicly available through the Illucidate repository."

---

## Questions?

- **About licensing:** See [CITATION.md](../../docs/CITATION.md)
- **Contributing data:** Open an issue or PR
- **Using data:** Read the dataset's README.md carefully

---

**Remember:** Proper attribution protects both you and the original researchers!
