"""
All constants specific to the application
"""
from os import getenv

PARAMS = {
    "TEMP_LABEL": getenv("TEMP_LABEL", "temperature"),
    "HUMIDITY_LABEL": getenv("HUMIDITY_LABEL", "humidity"),
    "SLEEP_INTERVAL": int(getenv("SLEEP_INTERVAL", 5)),
}
