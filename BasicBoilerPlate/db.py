import psycopg
from psycopg.errors import UniqueViolation, NotNullViolation
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("PGHOST"), 
    "port": os.getenv("PGPORT"),
    "dbname": os.getenv("PGDB"), 
    "user": os.getenv("PGUSERNAME"),
    "password": os.getenv("PGPASSWORD"),
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)

# CRUD operations for the "users" table

def insert_user():

def get_user():

def update_user():

def delete_user():

def main():
    return

if __name__ == "__main__":
    main()