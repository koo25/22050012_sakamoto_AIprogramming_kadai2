# weather_logic.py
import requests
import pandas as pd

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        data = response.json()
        current = data["current_condition"][0]
        weather_info = {
            "気温": current["temp_C"] + "°C",
            "体感温度": current["FeelsLikeC"] + "°C",
            "天気": current["weatherDesc"][0]["value"],
            "湿度": current["humidity"] + "%",
            "風速": current["windspeedKmph"] + " km/h"
        }

        # 日ごとの気温データ
        forecast = data["weather"]
        dates = []
        max_temps = []
        min_temps = []
        for day in forecast:
            dates.append(day["date"])
            max_temps.append(int(day["maxtempC"]))
            min_temps.append(int(day["mintempC"]))
        temp_df = pd.DataFrame({
            "日付": dates,
            "最高気温": max_temps,
            "最低気温": min_temps
        })
        return weather_info, temp_df
    except Exception:
        return None, None