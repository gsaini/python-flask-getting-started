import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Get a connection to the database."""
    try:
        conn = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        raise