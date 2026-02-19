import psycopg
from psycopg.errors import UniqueViolation, NotNullViolation
from dotenv import load_dotenv
import os
import bcrypt

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

def create_user(username, password):
    password = hash_password(password)
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    INSERT INTO users (username, password) 
                    VALUES (%s, %s)
                    """,
                    (username, password)
                )
                conn.commit()
            except UniqueViolation:
                print("User with that username already exists.")
            except NotNullViolation:
                print("Missing required fields.")

def get_user(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            return cur.fetchone()
        
def update_user(id, username, password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    UPDATE users 
                    SET username = %s, password = %s 
                    WHERE id = %s
                    """,
                    (username, password, id)
                )
                conn.commit()
            except UniqueViolation:
                print("User already exists.")
            except NotNullViolation:
                print("Missing required fields.")

def delete_user(username,password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("DELETE FROM users WHERE username = %s AND password = %s", (username,password))
                conn.commit()
            except:
                print("No user found with the provided username and password.")

def authenticate_user(username, password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            return cur.fetchone() is not None

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def show_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            print(cur.fetchall())

def clear_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users")
            conn.commit()

#######################################################################

def main():
    return 

if __name__ == "__main__":
    main()