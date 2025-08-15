# weather_app.py
import streamlit as st
import requests

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
        return weather_info
    except Exception as e:
        return None

# Streamlit UI
st.title("🌦️ 天気情報アプリ")
city = st.text_input("都市名を入力してください（例: Tokyo, Osaka, London）")

if st.button("天気を取得"):
    if city.strip():
        with st.spinner("取得中..."):
            weather = get_weather(city.strip())
        if weather:
            st.success(f"{city} の現在の天気")
            for key, value in weather.items():
                st.write(f"**{key}**: {value}")
        else:
            st.error("天気情報の取得に失敗しました。都市名を確認してください。")