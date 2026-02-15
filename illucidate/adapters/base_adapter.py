"""
Base adapter class for plate reader data parsers.

All plate reader adapters should inherit from this class and implement the parse() method.
"""

from pathlib import Path
from abc import ABC, abstractmethod
import pandas as pd


class BaseAdapter(ABC):
    """
    Abstract base class for plate reader adapters.
    
    All adapters must return data in standardized wide format:
        - Well: str (e.g., 'A1', 'B2', 'H12')
        - {Measurement}_T{N}_sec: float (e.g., 'OD600_T0_sec', 'OD600_T1_sec')
        - Time_{N}_seconds: float (timepoint in seconds)
        - Time_{N}_hours: float (timepoint in hours)
    
    Example output structure:
        | Well | OD600_T0_sec | OD600_T1_sec | ... | Time_0_seconds | Time_0_hours |
        |------|--------------|--------------|-----|----------------|--------------|
        | A1   | 0.05         | 0.06         | ... | 0.0            | 0.0          |
        | A2   | 0.05         | 0.07         | ... | 0.0            | 0.0          |
    """
    
    def __init__(self, filepath):
        """
        Initialize the adapter.
        
        Args:
            filepath: str or Path to the data file
        """
        self.filepath = Path(filepath)
        
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
    
    @abstractmethod
    def parse(self):
        """
        Parse the data file and return standardized DataFrame.
        
        Returns:
            pd.DataFrame: Standardized wide-format DataFrame with:
                - Well column (str)
                - Measurement columns ({Measurement}_T{N}_sec)
                - Time columns (Time_{N}_seconds and Time_{N}_hours)
        
        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Subclasses must implement parse()")
    
    def validate_output(self, df):
        """
        Validate that the parsed DataFrame meets the required format.
        
        Args:
            df: pd.DataFrame to validate
        
        Returns:
            bool: True if valid
        
        Raises:
            ValueError: If DataFrame doesn't meet requirements
        """
        # Check required columns
        if 'Well' not in df.columns:
            raise ValueError("DataFrame must have 'Well' column")
        
        # Check for time columns
        time_cols = [c for c in df.columns if 'Time_' in c and '_seconds' in c]
        if len(time_cols) == 0:
            raise ValueError("DataFrame must have Time_N_seconds columns")
        
        # Check for measurement columns
        measurement_cols = [c for c in df.columns if '_T' in c and '_sec' in c]
        if len(measurement_cols) == 0:
            raise ValueError("DataFrame must have measurement columns (e.g., OD600_T0_sec)")
        
        # Check well names are valid
        valid_wells = set()
        for row in 'ABCDEFGH':
            for col in range(1, 13):
                valid_wells.add(f"{row}{col}")
        
        invalid_wells = set(df['Well']) - valid_wells
        if invalid_wells and len(invalid_wells) > 0:
            print(f"Warning: Non-standard well names detected: {invalid_wells}")
        
        return True


def quick_parse(filepath, adapter_class=None, **kwargs):
    """
    Convenience function to quickly parse a file.
    
    Args:
        filepath: Path to data file
        adapter_class: Adapter class to use (auto-detected if None)
        **kwargs: Additional arguments passed to adapter
    
    Returns:
        pd.DataFrame: Parsed data in standard format
    
    Example:
        >>> from illucidate.adapters import quick_parse
        >>> df = quick_parse('data.xlsx')  # Auto-detect format
        >>> 
        >>> # Or specify adapter
        >>> from illucidate.adapters.victor_nivo import VictorNivoAdapter
        >>> df = quick_parse('data.xlsx', VictorNivoAdapter, Op4='OD600')
    """
    filepath = Path(filepath)
    
    # Auto-detect adapter if not specified
    if adapter_class is None:
        adapter_class = _detect_adapter(filepath)
    
    adapter = adapter_class(filepath, **kwargs)
    return adapter.parse()


def _detect_adapter(filepath):
    """
    Attempt to detect the appropriate adapter based on file characteristics.
    
    Args:
        filepath: Path to data file
    
    Returns:
        Adapter class
    
    Note:
        This is a simple heuristic. You may need to specify the adapter explicitly.
    """
    # Import here to avoid circular imports
    from illucidate.adapters.victor_nivo import VictorNivoAdapter
    from illucidate.adapters.generic_csv import GenericCSVAdapter
    
    suffix = filepath.suffix.lower()
    
    if suffix == '.csv':
        return GenericCSVAdapter
    elif suffix in ['.xlsx', '.xls']:
        # Try to detect Victor Nivo format
        # This is a simple check - might need refinement
        import pandas as pd
        try:
            df = pd.read_excel(filepath, header=None, nrows=50)
            # Victor Nivo files typically have "OPERATION" in early rows
            if df.astype(str).apply(lambda x: x.str.contains('OPERATION')).any().any():
                return VictorNivoAdapter
        except:
            pass
        
        # Default to generic
        return GenericCSVAdapter
    else:
        raise ValueError(f"Cannot auto-detect adapter for {suffix} files. Please specify adapter_class.")
