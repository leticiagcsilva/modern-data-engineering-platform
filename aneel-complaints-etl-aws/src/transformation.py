"""Transformation logic for standardizing ANEEL complaint data."""

import pandas as pd


def transform_aneel_complaints(complaints_df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names, enforce required fields, and parse dates."""
    standardized_df = complaints_df.copy()
    standardized_df.columns = [
        column.strip().lower().replace(" ", "_") for column in standardized_df.columns
    ]
    standardized_df = standardized_df.dropna(
        subset=["datreferencia", "qtdreclamacoesrecebidas"]
    )
    standardized_df["datreferencia"] = pd.to_datetime(
        standardized_df["datreferencia"], errors="coerce"
    )
    return standardized_df
