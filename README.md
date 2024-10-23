# Real-Time Weather Monitoring System with Rollups and Aggregates

## Objective
This project is a real-time weather data processing system that retrieves weather data from the OpenWeatherMap API for several Indian cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad). It processes, stores, and analyzes the data to provide daily summaries with rollups and aggregates and triggers alerts based on user-defined thresholds.

## Features
- **Real-Time Weather Data**: Continuously retrieves data from OpenWeatherMap at configurable intervals.
- **Temperature Conversion**: Converts temperatures from Kelvin to Celsius/Fahrenheit based on user preference.
- **Daily Weather Summaries**: Calculates daily aggregates (average, max, min temperature, dominant weather condition).
- **Alerts**: Triggers alerts based on user-defined temperature thresholds.
- **Visualizations**: Displays historical weather trends and daily summaries (alerts included).

## Data Source
We are using the [OpenWeatherMap API](https://openweathermap.org/) to fetch real-time weather updates.

### Weather Parameters
- **`main`**: Main weather condition (Rain, Snow, Clear, etc.)
- **`temp`**: Temperature in Kelvin (converted to Celsius/Fahrenheit).
- **`feels_like`**: Perceived temperature.
- **`dt`**: Timestamp for the weather update.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-monitoring.git
cd weather-monitoring
