"""Backward-compatible extraction wrapper."""

from src.ingestion import fetch_aneel_complaints


def extract_aneel_data():
    """Preserve the original extraction interface."""
    return fetch_aneel_complaints()
