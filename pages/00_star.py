import streamlit as st
import random

st.set_page_config(page_title="✨ 반짝별 놀이터 ✨", layout="centered")
st.title("✨ 반짝별 놀이터 ✨")
st.write("버튼을 누르면 랜덤한 반짝별이 나타나요! 🌟")

colors = ["#FF4B4B", "#4BFF6B", "#4BB3FF", "#FFEA4B", "#FF7BFF", "#8D4BFF"]
stars = ["🌟", "✨", "💫", "⭐", "🌠"]

def generate_stars():
    star_count = random.randint(5, 15)  # 별 개수 랜덤
    star_display = ""
    for _ in range(star_count):
        star = random.choice(stars)
        color = random.choice(colors)
        star_display += f"<span style='color:{color}; font-size:{random.randint(20,50)}px'>{star}</span> "
    st.markdown(star_display, unsafe_allow_html=True)

if st.button("🌌 반짝별 생성!"):
    generate_stars()

st.write("같은 버튼을 여러 번 눌러보세요! 매번 다른 색과 모양의 별이 나타나요 😎")
