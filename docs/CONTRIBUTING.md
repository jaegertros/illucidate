# Contributing to Illucidate

Thank you for your interest in contributing! Illucidate is designed to be **modular and extensible**.

## Ways to Contribute

1. **Add plate reader adapters** - Support for new instruments
2. **Implement new features** - Additional signal processing methods
3. **Improve documentation** - Examples, tutorials, clarifications
4. **Report bugs** - Help us improve quality
5. **Share datasets** - With proper attribution

---

## Adding a New Plate Reader Adapter

This is one of the most valuable contributions! Here's how:

### Step 1: Understand the Base Adapter

All adapters inherit from `BaseAdapter`:

```python
from illucidate.adapters.base_adapter import BaseAdapter

class YourReaderAdapter(BaseAdapter):
    def parse(self):
        """
        Parse the file and return a standardized DataFrame.
        
        Returns:
            pd.DataFrame with columns:
                - Well: str (e.g., 'A1', 'B2')
                - {Measurement}_T{N}_sec: float values
                - Time_{N}_seconds: float (timepoint in seconds)
                - Time_{N}_hours: float (timepoint in hours)
        """
        pass
```

### Step 2: Study the File Format

Open an export file from your plate reader and note:
- How are wells organized? (Rows? Columns? List format?)
- Where are the measurement names? (OD600, RLU, etc.)
- Where are the time points?
- Are there multiple measurements in one file?
- Is there metadata (temperature, reader settings)?

### Step 3: Implement the Parser

```python
import pandas as pd
import numpy as np
from pathlib import Path
from illucidate.adapters.base_adapter import BaseAdapter

class BioTekSynergyAdapter(BaseAdapter):
    """
    Adapter for BioTek Synergy H1/H4 plate readers.
    
    Expected format:
    - Excel file (.xlsx) with separate sheets for each measurement
    - Sheet names: "OD600", "Lum", etc.
    - Data in 96-well grid format (rows A-H, columns 1-12)
    - Time in first row
    """
    
    def __init__(self, filepath, measurement_labels=None):
        super().__init__(filepath)
        self.measurement_labels = measurement_labels or {}
        
    def parse(self):
        """Parse BioTek Synergy export file."""
        print(f"Parsing BioTek file: {self.filepath.name}")
        
        # Load Excel file
        excel_file = pd.ExcelFile(self.filepath)
        
        all_data = {}
        
        # Process each sheet (each measurement type)
        for sheet_name in excel_file.sheet_names:
            if sheet_name in ['Settings', 'Layout']:  # Skip metadata
                continue
                
            # Read sheet
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            
            # Extract time points (usually in first row)
            times = self._extract_times(df)
            
            # Extract well data
            well_data = self._extract_wells(df, times, sheet_name)
            
            # Label the measurement
            measurement_name = self.measurement_labels.get(sheet_name, sheet_name)
            all_data[measurement_name] = well_data
        
        # Merge all measurements into wide format
        consolidated = self._merge_measurements(all_data)
        
        print(f"✓ Parsed {len(consolidated)} wells, {len(consolidated.columns)} columns")
        return consolidated
    
    def _extract_times(self, df):
        """Extract time points from the data."""
        # Implementation depends on exact format
        # Example: times might be in row 0, columns 1+
        times = []
        # ... your parsing logic here ...
        return times
    
    def _extract_wells(self, df, times, measurement_name):
        """Extract well values."""
        well_data = []
        
        # Example: iterate through rows A-H
        for row_letter in 'ABCDEFGH':
            for col_num in range(1, 13):
                well_name = f"{row_letter}{col_num}"
                
                # Extract values for this well
                values = []  # ... get values from df ...
                
                # Create row dict
                row_dict = {'Well': well_name}
                for t_idx, val in enumerate(values):
                    row_dict[f'T{t_idx}_sec'] = val
                
                well_data.append(row_dict)
        
        df = pd.DataFrame(well_data)
        df.attrs['times'] = times
        return df
    
    def _merge_measurements(self, all_data):
        """Merge multiple measurement types into wide format."""
        base_df = None
        
        for measurement_type, df in all_data.items():
            if base_df is None:
                base_df = df[['Well']].copy()
            
            # Rename columns to include measurement type
            renamed = df.copy()
            for col in df.columns:
                if col != 'Well':
                    renamed.rename(columns={col: f'{measurement_type}_{col}'}, inplace=True)
            
            base_df = base_df.merge(renamed, on='Well', how='outer')
        
        # Add time columns
        first_measurement = list(all_data.values())[0]
        times = first_measurement.attrs.get('times', [])
        
        for idx, time_sec in enumerate(times):
            base_df[f'Time_{idx}_seconds'] = time_sec
            base_df[f'Time_{idx}_hours'] = time_sec / 3600
        
        return base_df
```

### Step 4: Add Tests

Create `tests/test_biotek_adapter.py`:

```python
import pytest
from illucidate.adapters.biotek import BioTekSynergyAdapter

def test_biotek_adapter():
    adapter = BioTekSynergyAdapter('examples/data/biotek_example.xlsx')
    df = adapter.parse()
    
    # Check basic structure
    assert 'Well' in df.columns
    assert len(df) == 96  # 96-well plate
    
    # Check measurements are present
    assert any('OD' in col for col in df.columns)
    
    # Check time columns
    assert any('Time_' in col for col in df.columns)
```

### Step 5: Add Documentation

Create an example in `examples/` showing how to use your adapter.

### Step 6: Submit Pull Request

1. Fork the repository
2. Create a new branch: `git checkout -b add-biotek-adapter`
3. Add your adapter: `illucidate/adapters/biotek.py`
4. Add tests: `tests/test_biotek_adapter.py`
5. Add example data (if possible): `examples/data/biotek_example.xlsx`
6. Update README to list your adapter
7. Commit: `git commit -m "Add BioTek Synergy adapter"`
8. Push: `git push origin add-biotek-adapter`
9. Open pull request on GitHub

---

## Adding New Features

Want to add a new feature extraction method?

### Location
Add to `illucidate/core/feature_generator.py`

### Pattern

```python
def generate_your_feature(self, values, measurement_type):
    """
    Generate your custom feature.
    
    Args:
        values: np.array of measurement values over time
        measurement_type: str (e.g., 'OD600')
    
    Returns:
        dict of {feature_name: feature_value}
    """
    features = {}
    
    # Your feature calculation
    # Example: Find the steepest slope
    slopes = np.diff(values)
    max_slope = np.max(slopes)
    
    features[f'{measurement_type}_max_slope'] = max_slope
    
    return features
```

### Add to Pipeline

In `FeatureGenerator.generate_all_features()`:

```python
# Add your feature
custom_features = self.generate_your_feature(values, mtype)
feature_row.update(custom_features)
```

---

## Code Style

- Use **Black** for formatting: `black illucidate/`
- Follow **PEP 8** naming conventions
- Add **docstrings** to all functions
- Include **type hints** where helpful
- Write **tests** for new functionality

---

## Example Datasets

Contributing example data? Great!

### Requirements:
1. You own the data OR have permission
2. Choose appropriate license (CC0, CC-BY, CC-BY-NC)
3. Include complete README.md with:
   - Citation information
   - License
   - Experimental details
   - File descriptions

### Location
`examples/data/[your_dataset]/`

### Template README:

```markdown
# Dataset Name

## Source
- Publication: [Citation]
- DOI: [DOI or "Unpublished"]
- License: [CC0 / CC-BY-4.0 / etc.]

## Citation
If you use this data, cite: [Full citation]

## Details
- Organism: [Species]
- Measurements: [OD, RLU, etc.]
- Instrument: [Reader model]
- Duration: [X hours, Y timepoints]

## Files
- data.xlsx - Raw export
- experimental_design.csv - Well annotations
```

---

## Reporting Bugs

Found a bug? Please open an issue with:

1. **Descriptive title**
2. **Steps to reproduce**
3. **Expected behavior**
4. **Actual behavior**
5. **Your setup:**
   - Python version
   - Illucidate version
   - Operating system
   - Plate reader model

---

## Questions?

- Open an issue for discussions
- Check existing issues first
- Be respectful and constructive

Thank you for contributing to Illucidate! 🚩
