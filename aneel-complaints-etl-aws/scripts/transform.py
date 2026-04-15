import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.dropna(subset=["datreferencia", "qtdreclamacoesrecebidas"])
    df["datreferencia"] = pd.to_datetime(df["datreferencia"], errors="coerce")
    return df
