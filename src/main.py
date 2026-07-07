from src.extract import extract_data
from src.validate import validate_data
from src.transform import transform_data
from src.load import load_data
from src.logger import logger

logger.info("Starting Cloud Ready ETL Pipeline...")

df = extract_data()
df = validate_data(df)
df = transform_data(df)
load_data(df)

logger.success("ETL Pipeline Completed Successfully.")