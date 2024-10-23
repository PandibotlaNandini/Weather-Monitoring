import time
from config import CITIES, INTERVAL, TEMPERATURE_UNIT
from api_client import get_weather_data
from data_processor import process_weather_data
from alert_manager import check_alert_conditions

def main():
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                processed_data = process_weather_data(weather_data, unit=TEMPERATURE_UNIT)
                check_alert_conditions(processed_data)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
