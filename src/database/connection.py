import duckdb
import streamlit as st

@st.cache_resource
def get_connection():
    """
    Gets a once connection with Duckdb.
    The cache_resouce guarantee that connection persists.

    Returns:
        DuckDBPyConnection: A object of active connection.
    """
    return duckdb.connect(database='data/db_local.duck.db', read_only=False)

def init_db():
    con = get_connection()
    return con