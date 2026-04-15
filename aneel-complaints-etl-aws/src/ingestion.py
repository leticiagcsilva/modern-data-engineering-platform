"""Ingestion utilities for retrieving ANEEL complaint data from the CKAN API."""

from typing import Any

import pandas as pd
import requests


ANEEL_DATASTORE_URL = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search"
ANEEL_RESOURCE_ID = "53f14a30-d206-4bee-b1bc-c8eb50f84b7f"


def fetch_aneel_complaints(limit: int = 1000) -> pd.DataFrame:
    """Fetch complaint records from the public ANEEL CKAN datastore API."""
    params: dict[str, Any] = {
        "resource_id": ANEEL_RESOURCE_ID,
        "limit": limit,
    }
    response = requests.get(ANEEL_DATASTORE_URL, params=params, timeout=30)
    response.raise_for_status()

    payload = response.json()
    records = payload["result"]["records"]
    return pd.DataFrame.from_records(records)
