import pandas as pd

def clean_dataset(df: pd.DataFrame):
    df = df.dropna()
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df
