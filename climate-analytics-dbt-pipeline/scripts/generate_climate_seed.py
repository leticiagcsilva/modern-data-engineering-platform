"""Generate a reproducible CSV seed with daily climate observations."""

from pathlib import Path

import pandas as pd
import requests


CITIES = [
    {"city": "Aracaju", "state": "SE", "lat": -10.9472, "lon": -37.0731},
    {"city": "Fortaleza", "state": "CE", "lat": -3.7172, "lon": -38.5433},
    {"city": "João Pessoa", "state": "PB", "lat": -7.1195, "lon": -34.845},
    {"city": "Maceió", "state": "AL", "lat": -9.6658, "lon": -35.735},
    {"city": "Natal", "state": "RN", "lat": -5.7945, "lon": -35.211},
    {"city": "Recife", "state": "PE", "lat": -8.0476, "lon": -34.877},
    {"city": "Salvador", "state": "BA", "lat": -12.9718, "lon": -38.5011},
    {"city": "São Luís", "state": "MA", "lat": -2.5307, "lon": -44.3068},
    {"city": "Teresina", "state": "PI", "lat": -5.0892, "lon": -42.8016},
]

START_DATE = "2020-01-01"
END_DATE = "2024-12-31"
OUTPUT_PATH = Path("seeds/daily_climate_northeast_capitals.csv")


def fetch_city_climate(city_metadata: dict) -> pd.DataFrame:
    """Fetch daily climate observations for one city."""
    print(f"Downloading data for {city_metadata['city']} ({city_metadata['state']})...")
    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={city_metadata['lat']}&longitude={city_metadata['lon']}"
        f"&start_date={START_DATE}&end_date={END_DATE}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&timezone=America%2FSao_Paulo"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    payload = response.json()

    climate_df = pd.DataFrame(
        {
            "date": payload["daily"]["time"],
            "temperature_max": payload["daily"]["temperature_2m_max"],
            "temperature_min": payload["daily"]["temperature_2m_min"],
            "precipitation": payload["daily"]["precipitation_sum"],
        }
    )
    climate_df["city"] = city_metadata["city"]
    climate_df["state"] = city_metadata["state"]
    return climate_df


def main() -> None:
    """Persist the extracted climate dataset as a CSV seed."""
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    city_frames = []

    for city_metadata in CITIES:
        try:
            city_frames.append(fetch_city_climate(city_metadata))
        except Exception as exc:
            print(f"Error while processing {city_metadata['city']}: {exc}")

    if not city_frames:
        print("No data was downloaded.")
        return

    result = pd.concat(city_frames, ignore_index=True)
    result.to_csv(OUTPUT_PATH, index=False)
    print(f"Seed saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
