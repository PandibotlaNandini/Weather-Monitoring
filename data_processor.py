def kelvin_to_celsius(temp):
    return temp - 273.15

def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

def process_weather_data(data, unit="Celsius"):
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    if unit == "Celsius":
        temp = kelvin_to_celsius(temp)
        feels_like = kelvin_to_celsius(feels_like)
    else:
        temp = kelvin_to_fahrenheit(temp)
        feels_like = kelvin_to_fahrenheit(feels_like)

    return {
        "city": data["name"],
        "temperature": round(temp, 2),
        "feels_like": round(feels_like, 2),
        "main_condition": data["weather"][0]["main"],
        "timestamp": data["dt"]
    }
