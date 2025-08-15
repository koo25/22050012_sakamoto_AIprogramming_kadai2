# app.py
import streamlit as st
from logic import get_weather

st.title("天気情報アプリ + 気温グラフ")
city = st.text_input("都市名を入力してください（例: Tokyo, Osaka, London）")

if st.button("天気を取得"):
    if city.strip():
        with st.spinner("取得中..."):
            weather, temp_df = get_weather(city.strip())
        if weather:
            st.success(f"{city} の現在の天気")
            for key, value in weather.items():
                st.write(f"**{key}**: {value}")

            st.subheader("今後数日の気温推移")
            st.line_chart(temp_df.set_index("日付"))
        else:
            st.error("天気情報の取得に失敗しました。都市名を確認してください。")