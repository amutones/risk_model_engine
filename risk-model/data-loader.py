"""
data_loader.py

Purpose:
    - Load portfolio CSV
    - Validate required columns
    - Convert numeric fields
    - Return a clean DataFrame for downstream modules
"""
import pandas as pd
from os.path import exists

REQUIRED_COLS = ["ticker","quantity","price","asset_class","sector","region","currency","duration","beta"]

def load_portfolio(path: str) -> pd.DataFrame:
    """
    Load portfolio CSV and validate schema
    """
    df = pd.read_csv(path)
    missing = set(REQUIRED_COLS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    return df

def load_factor_returns(path: str) -> pd.DataFrame:
    """
    Load factor returns from CSV
    """

    pass