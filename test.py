import os
import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUX_URL = os.environ.get("INFLUX_URL")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_ORG = os.environ.get("INFLUX_ORG")
INFLUX_BUCKET = os.environ.get("INFLUX_BUCKET")

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

print("Sending 10 test points to InfluxDB Cloud...")

for i in range(10):
    val = random.randint(100, 900)
    point = (
        Point("cloud_test_measurement")
        .tag("source", "github_actions")
        .field("analog_value", val)
    )
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
    print(f"[{i+1}/10] Sent: {val}")
    time.sleep(1)

client.close()
print("Done!")
