from influxdb_client import InfluxDBClient
import os

def get_influxdb_client():
    return InfluxDBClient(
        url=os.getenv("INFLUXDB_URL"),
        token=os.getenv("INFLUXDB_TOKEN"),
        org=os.getenv("INFLUXDB_ORG")
    )
