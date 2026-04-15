import requests
import pandas as pd

def extract_aneel_data():
    url = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search"
    params = {
        "resource_id": "53f14a30-d206-4bee-b1bc-c8eb50f84b7f",
        "limit": 1000
    }
    response = requests.get(url, params=params)
    records = response.json()["result"]["records"]
    df = pd.DataFrame.from_records(records)
    return df
