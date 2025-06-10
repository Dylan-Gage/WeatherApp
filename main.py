import requests
from datetime import date, timedelta

city_name = "New York"

weather_url = "https://api.open-meteo.com/v1/forecast"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {"name":city_name}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

if geo_data["results"]:
    result = geo_data["results"][0]
    lat = result["latitude"]
    lon = result["longitude"]

    today = date.today()
    end_day = today + timedelta(days=6)

    weather_params = { 
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "start_date": today.isoformat(),
        "end_date": end_day.isoformat(),
        }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    print(f'7-Day Forecast for {city_name}:\n ')
    for day, t_max, t_min in zip(weather_data['daily']['time'], 
                                 weather_data['daily']['temperature_2m_max'], 
                                 weather_data['daily']['temperature_2m_min']):
        print(f"{day}: High {t_max}°C, Low {t_min}°C")
else:
    print("City not found.")



