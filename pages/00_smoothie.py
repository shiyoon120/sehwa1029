import streamlit as st
import random

st.title("🍓 오늘의 나만의 스무디 🍓")
st.write("기분과 맛을 선택하면, 랜덤으로 나만의 스무디를 추천해드려요!")

# 사용자 입력
mood = st.selectbox("오늘 기분 선택", ["행복 😄", "우울 😢", "활기 😎", "평온 😌"])
taste = st.selectbox("선호하는 맛", ["달콤 🍯", "상큼 🍋", "신선 🌿", "시원 ❄️"])

if st.button("🥤 스무디 추천받기"):
    colors = ["빨강 ❤️", "주황 🧡", "노랑 💛", "초록 💚", "파랑 💙", "보라 💜", "분홍 💖"]
    smoothies = [
        "딸기 바나나 스무디 🍓🍌",
        "망고 파인애플 스무디 🥭🍍",
        "블루베리 요거트 스무디 🫐",
        "키위 사과 스무디 🥝🍏",
        "레몬 민트 스무디 🍋🌿",
        "복숭아 요거트 스무디 🍑"
    ]
    descriptions = [
        "오늘 기분을 상큼하게 만들어 줄 달콤한 한 잔!",
        "에너지를 충전해주는 활기찬 스무디",
        "편안한 휴식과 함께 즐기는 시원한 맛",
        "머릿속까지 상쾌하게 해주는 한 잔",
        "상큼함과 달콤함의 완벽한 조화",
        "건강까지 생각한 맛있는 스무디"
    ]
    
    chosen_smoothie = random.choice(smoothies)
    chosen_color = random.choice(colors)
    chosen_desc = random.choice(descriptions)
    
    st.markdown(f"### 오늘의 스무디 추천 🥤")
    st.markdown(f"**색깔:** {chosen_color}")
    st.markdown(f"**스무디 이름:** {chosen_smoothie}")
    st.markdown(f"**설명:** {chosen_desc}")
