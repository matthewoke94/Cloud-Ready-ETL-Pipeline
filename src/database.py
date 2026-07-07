from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///cloud_ready_etl.db"

engine = create_engine(DATABASE_URL)