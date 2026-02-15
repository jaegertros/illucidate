# Citation Guidelines

## Citing Illucidate

If you use Illucidate in your research, please cite:

```bibtex
@software{illucidate2025,
  title = {Illucidate: Illuminating early signals in bacterial detection},
  author = {Waddell, Caleb L.},
  year = {2025},
  url = {https://github.com/jaegertros/illucidate},
  version = {0.1.0},
  note = {Open-source toolkit for multivariate analysis of time-series biosensor data}
}
```

---

## About the Name

**Illucidate** = *Illuminate* + *Elucidate*

The name pays homage to the bioluminescent reporter phages (ΦV10::NanoLuc and ΦV10::lux) that inspired this work—literally *illuminating* bacterial presence while *elucidating* hidden patterns in the data.

---

## Citing Data Sources

**CRITICAL:** If you use published datasets with Illucidate, you **must** cite the original publications.

### Example: Proper Attribution

✅ **CORRECT:**

> "We applied Illucidate (Waddell, 2025) to analyze multivariate detection patterns in published bioluminescent reporter phage data (Meile et al., 2023; Alonzo et al., 2022). Raw time-series data were obtained from supplementary materials with permission from the authors..."

✅ **CORRECT (in methods):**

> "Publicly available data from [Study X] were reanalyzed using Illucidate to identify early multivariate signals. Original data are available at [URL] and were used with permission under [License]."

❌ **INCORRECT:**

> "We analyzed data using Illucidate..." (No mention of original data source)

---

## Data Attribution Requirements

### If you use example data from `/examples/data/`:

**Each dataset has a README.md with:**
- Original publication citation
- Data source/URL
- License information
- Any usage restrictions
- How to cite the original work

**You must:**
1. Read the dataset's README.md
2. Cite the original publication
3. Follow any license requirements
4. Acknowledge data providers

### If you use your own data:

**You should:**
1. Document your data collection methods
2. Include metadata (experimental conditions, instruments used)
3. Consider making data available (Figshare, Zenodo, etc.)
4. Specify any usage restrictions

### If you obtain data directly from authors:

**Best practices:**
1. Get explicit permission to use and publish analyses
2. Offer co-authorship if substantial new insights emerge
3. Acknowledge data providers in your paper
4. Share your analysis results with them
5. Follow any embargo or confidentiality agreements

---

## Example Acknowledgments

### For Conference Abstracts:

> "Analysis was performed using the open-source Illucidate toolkit (Waddell, 2025). We thank Dr. [Name] for sharing raw data from [Study]."

### For Journal Articles:

> "Multivariate feature extraction and statistical analysis were performed using Illucidate v0.1.0 (Waddell, 2025), an open-source Python toolkit available at https://github.com/jaegertros/illucidate. Published datasets were obtained from [citations] and analyzed with permission from the authors."

### For Theses/Dissertations:

> "Computational analysis was enabled by the Illucidate software package (Waddell, 2025), which implements autonomous feature generation and statistical testing for time-series biosensor data. Raw data from published studies were obtained from supplementary materials or by direct request to corresponding authors, and all analyses comply with original data licenses."

---

## Contributing Data to Illucidate

Want to contribute example datasets? Great! Here's how:

### Requirements:

1. **You own the data** OR have explicit permission to share
2. **Choose an appropriate license:**
   - CC0 (public domain)
   - CC-BY 4.0 (attribution required)
   - CC-BY-NC 4.0 (non-commercial use only)
3. **Provide complete metadata:**
   - Experimental conditions
   - Instrument/settings used
   - Date collected
   - Publication reference (if published)
4. **Include a README.md** in the dataset folder

### Example Dataset README:

```markdown
# Dataset: E. coli O157:H7 Detection with NanoLuc Reporter Phage

## Source
Published in: [Citation]
DOI: [DOI]
Original data: [URL or "Unpublished"]

## License
CC-BY 4.0 - Attribution required

## Citation
If you use this data, cite:
[Full citation]

## Experimental Details
- Organism: E. coli O157:H7
- Phage: ΦV10-NanoLuc
- Instrument: Victor Nivo plate reader
- Measurements: OD600, OD560, Bioluminescence
- Duration: 12 hours, 60 timepoints
- Conditions: See original publication

## Files
- raw_data.xlsx - Original Victor Nivo export
- experimental_design.csv - Well annotations
- README.md - This file
```

---

## License Compatibility

Illucidate is released under the **MIT License**, which allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**BUT** you must:
- ✅ Include the original copyright notice
- ✅ Include the license text

**Note:** Data you analyze with Illucidate retains its original license. Illucidate's MIT license applies to the software only, not to data.

---

## Questions?

- License questions: See [LICENSE](../LICENSE)
- Data contribution: Open an issue or PR
- Citation format: Adapt examples above to your field's style guide

---

**Remember:** Proper attribution protects both you and the original researchers. When in doubt, over-cite rather than under-cite!
