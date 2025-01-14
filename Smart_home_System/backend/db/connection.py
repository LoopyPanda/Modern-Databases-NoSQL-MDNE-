import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extras import DictCursor
from psycopg2 import OperationalError
import redis
from influxdb_client import InfluxDBClient
import os



# PostgreSQL Connection

def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database using environment variables.
    Returns:
        psycopg2.extensions.connection: Database connection object.
    Raises:
        RuntimeError: If the connection to PostgreSQL fails.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "postgres"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            dbname=os.getenv("POSTGRES_DB", "smart_home"),
            user=os.getenv("POSTGRES_USER", "postgres_user"),
            password=os.getenv("POSTGRES_PASSWORD", "12345"),
            cursor_factory=DictCursor,  # Use DictCursor for cleaner data handling
        )
        return connection
    except OperationalError as e:
        raise RuntimeError(f"Error connecting to PostgreSQL: {e}")


# Redis Connection
def get_redis_client():
    """
    Get a Redis client connection.
    """
    try:
        client = redis.StrictRedis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            decode_responses=True
        )
        return client
    except Exception as e:
        raise RuntimeError(f"Error connecting to Redis: {e}")

# InfluxDB Connection
def get_influxdb_client():
    """
    Get an InfluxDB client connection.
    """
    try:
        client = InfluxDBClient(
            url=os.getenv("INFLUXDB_URL", "http://localhost:8086"),
            token=os.getenv("INFLUXDB_TOKEN", "your_token"),
            org=os.getenv("INFLUXDB_ORG", "your_org")
        )
        return client
    except Exception as e:
        raise RuntimeError(f"Error connecting to InfluxDB: {e}")


