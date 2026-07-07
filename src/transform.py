import pandas as pd

def transform_data(df):
    df["sales"] = df["sales"].round(2)
    df["country"] = df["country"].str.upper()
    return df