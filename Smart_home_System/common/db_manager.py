import psycopg2
from psycopg2.extras import DictCursor
import os

# PostgreSQL connection details
PG_HOST = os.getenv('POSTGRES_HOST', 'localhost')
PG_PORT = int(os.getenv('POSTGRES_PORT', 5432))
PG_DB = os.getenv('POSTGRES_DB', 'smart_home')
PG_USER = os.getenv('POSTGRES_USER', 'user')
PG_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')

# Create a database connection
def get_db_connection():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASSWORD
    )

# Fetch all houses
def fetch_houses():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id FROM houses;")
    houses = cursor.fetchall()
    conn.close()
    return [row['id'] for row in houses]

# Fetch a house by user ID
def fetch_house_by_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id FROM houses WHERE user_id = %s;", (user_id,))
    house = cursor.fetchone()
    conn.close()
    return house['id'] if house else None