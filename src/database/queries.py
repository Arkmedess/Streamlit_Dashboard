import pandas as pd
import duckdb
import os 
from src.database.connection import get_connection
from src.models.schema import settings

def excel_to_parquet(file_path: str):

    if not os.path.exists(settings.parquet_path):
        try:
            df = pd.read_excel(settings.excel_path, engine='calamine')
        
        except ImportError:
            df = pd.read_excel(settings.excel_path, engine='openpyxl')

    df = df.convert_dtypes(dtype_backend="pyarrow")

    df.to_parquet(settings.parquet_path, engine='pyarrow', index=False)