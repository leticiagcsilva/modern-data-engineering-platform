"""Backward-compatible transformation wrapper."""

import pandas as pd

from src.transformation import transform_aneel_complaints


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preserve the original transformation interface."""
    return transform_aneel_complaints(df)
