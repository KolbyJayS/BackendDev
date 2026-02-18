import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg.connect(
    dbname=os.getenv("PGDB"), 
    user=os.getenv("PGUSERNAME"),
    password=os.getenv("PGPASSWORD"),
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT"),
)

with conn:
    with conn.cursor() as cur:
        with open("schema.sql", "r") as f:
            cur.execute(f.read())