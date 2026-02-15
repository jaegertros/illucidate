# Getting Started with Illucidate

## Quick Start (5 minutes)

### Option 1: Google Colab (Zero Setup)

1. Click: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[your-username]/illucidate/blob/main/notebooks/01_quickstart_colab.ipynb)

2. Upload your Victor Nivo file when prompted

3. Define your experimental variables

4. Run the cells - get results!

### Option 2: Local Installation

```bash
# Clone repository
git clone https://github.com/[your-username]/illucidate.git
cd illucidate

# Install
pip install -e .

# Or just requirements
pip install -r requirements.txt
```

---

## Your First Analysis

### 1. Prepare Your Data

Illucidate needs:
- ✅ Your plate reader export file (Excel, CSV)
- ✅ Experimental design (what's in each well)

### 2. Choose Your Adapter

```python
from illucidate.adapters import quick_parse

# Auto-detect format
df = quick_parse('my_experiment.xlsx')

# Or specify adapter
from illucidate.adapters.victor_nivo import VictorNivoAdapter
df = quick_parse('my_experiment.xlsx', 
                 VictorNivoAdapter,
                 Op4='OD600',
                 Op5='OD560',
                 Op6='RLU')
```

### 3. Define Experimental Design

```python
experimental_design = {
    'A1': {'bacteria': 'E.coli_O157H7', 'phage': 'Yes', 'replicate': 1},
    'A2': {'bacteria': 'E.coli_O157H7', 'phage': 'Yes', 'replicate': 2},
    'B1': {'bacteria': 'E.coli_O157H7', 'phage': 'No', 'replicate': 1},
    # ... continue for all wells
}
```

### 4. Generate Features

```python
from illucidate.core import FeatureGenerator

generator = FeatureGenerator(df, experimental_design)
features = generator.generate_all()

print(f"Generated {len(features.columns)} features!")
```

### 5. Find Early Signals

```python
from illucidate.core import find_early_signals

# Compare wells with vs without phage
signals = find_early_signals(features, compare_variable='phage')

# View top signals
print(signals.head(10))
```

### 6. Visualize Results

```python
from illucidate.core import plot_growth_curves, plot_signal_rankings

# Growth curves colored by phage status
plot_growth_curves(df, experimental_design, color_by='phage')

# Top discriminative features
plot_signal_rankings(signals, top_n=20)
```

---

## Common Workflows

### Workflow 1: Screen for Best Phage

```python
# Compare multiple phages
experimental_design = {
    'A1-A4': {'bacteria': 'E.coli', 'phage': 'T4'},
    'B1-B4': {'bacteria': 'E.coli', 'phage': 'T7'},
    'C1-C4': {'bacteria': 'E.coli', 'phage': 'Lambda'},
}

signals = find_early_signals(features, compare_variable='phage')
# Which phage gives earliest detection?
```

### Workflow 2: Optimize Bacterial Concentration

```python
experimental_design = {
    'A1': {'concentration': '1e8'},
    'A2': {'concentration': '1e7'},
    'A3': {'concentration': '1e6'},
    # ...
}

signals = find_early_signals(features, compare_variable='concentration')
# What's the lowest detectable concentration?
```

### Workflow 3: Test Phage + Antibiotic Synergy

```python
from illucidate.core import analyze_interactions

# Does phage work better with antibiotics?
interaction = analyze_interactions(features, 
                                   var1='phage_present',
                                   var2='antibiotic',
                                   outcome='OD600_time_to_20x')
# Heatmap shows best combinations
```

---

## Understanding the Output

### Feature Types Generated:

**Early timepoint stats:**
- `OD600_early5_mean` - Average of first 5 timepoints
- `OD600_early10_slope` - Growth rate in first 10 timepoints

**Lag detection:**
- `OD600_time_to_11x` - When OD reaches 1.1× baseline
- `OD600_time_to_20x` - When OD reaches 2.0× baseline

**Growth characteristics:**
- `OD600_max_growth_rate` - Maximum rate of change
- `OD600_time_to_max_rate` - When max rate occurs

**Cross-measurement:**
- `OD600_div_OD560_mean` - Average ratio
- `OD600_div_RLU_early` - Early ratio pattern

### Statistical Output:

```
feature                    p_value    effect_size
OD600_time_to_12x         1.2e-08    31.5
OD600_early5_slope        3.4e-06    12.3
OD600_div_OD560_early     8.7e-05     8.9
```

**Effect size interpretation:**
- < 0.5: Small difference
- 0.5-1.0: Medium difference
- 1.0-2.0: Large difference
- \> 2.0: **Very large** - strong discriminative power

---

## Tips & Best Practices

### ✅ DO:
- Include replicates (3+ per condition minimum)
- Include proper controls (blanks, negative controls)
- Label all wells in experimental design
- Check raw data plots before analysis
- Start with simple comparisons

### ❌ DON'T:
- Analyze without replicates (unreliable statistics)
- Skip controls (can't validate signals)
- Trust signals without biological plausibility
- Over-interpret small effect sizes
- Use signals on completely different experimental conditions without validation

---

## Troubleshooting

**Problem:** "File not found"
→ Check file path, use absolute paths if needed

**Problem:** "No significant signals found"
→ Check if there are real differences in your data
→ Try different comparison variables
→ Ensure you have replicates

**Problem:** "Too many features"
→ Filter by effect size > 1.0 first
→ Focus on early-only features (`is_early == True`)

**Problem:** "Adapters not working"
→ Check file format matches expected adapter
→ Try GenericCSVAdapter for custom formats
→ See CONTRIBUTING.md for adding new adapters

---

## Next Steps

1. ✅ Run on your own data
2. ✅ Try different experimental variables
3. ✅ Validate top signals manually
4. ✅ Consider running on published datasets
5. ✅ Share your findings!

---

## Need Help?

- **Documentation:** See `docs/` folder
- **Examples:** See `examples/` folder  
- **Issues:** [GitHub Issues](https://github.com/[your-username]/illucidate/issues)
- **Discussions:** [GitHub Discussions](https://github.com/[your-username]/illucidate/discussions)

Happy analyzing! 🚩
