from src.database import engine

def load_data(df):
    df.to_sql(
        "sales_data",
        con=engine,
        if_exists="replace",
        index=False
    )