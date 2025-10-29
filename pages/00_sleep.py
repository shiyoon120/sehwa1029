import streamlit as st
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="🌙 나만의 수면 분석기", page_icon="🌙", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #89f7fe, #66a6ff);
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌙 나만의 수면 분석기")
st.write("수면 시작과 기상 시간을 입력하면 오늘 나의 컨디션을 알려드려요!")

# 입력
with st.container():
    sleep_time = st.time_input("💤 잠든 시간", value=datetime.strptime("23:00", "%H:%M").time())
    wake_time = st.time_input("⏰ 기상 시간", value=datetime.strptime("07:30", "%H:%M").time())
    mood = st.selectbox("오늘 기분 선택", ["좋음 😄", "보통 😐", "졸림 😴", "활기 😎"])

if st.button("📝 컨디션 확인"):
    # 시간 계산
    sleep_dt = datetime.combine(datetime.today(), sleep_time)
    wake_dt = datetime.combine(datetime.today(), wake_time)
    if wake_dt <= sleep_dt:  # 다음날로 넘어가는 경우
        wake_dt += timedelta(days=1)
    sleep_hours = (wake_dt - sleep_dt).seconds / 3600

    # 수면 상태
    if sleep_hours >= 8:
        sleep_msg = "푹 잤네요! 오늘 하루 활기차게 보내세요! 🌞"
        card_color = "#fffa87"  # 밝은 노랑
        emoji = "☀️"
    elif 6 <= sleep_hours < 8:
        sleep_msg = "충분히 잤지만 조금 피곤할 수 있어요. ☁️"
        card_color = "#87cefa"  # 하늘색
        emoji = "🌤️"
    else:
        sleep_msg = "조금 부족한 잠! 오늘은 무리하지 말고 쉬세요. 💤"
        card_color = "#a9a9a9"  # 회색
        emoji = "🌙"

    # 기분 메시지
    mood_msg = {
        "좋음 😄": "기분 좋으니 오늘은 새로운 걸 도전해보세요! ✨",
        "보통 😐": "평온하게, 일상의 루틴을 지켜보세요. 🛋️",
        "졸림 😴": "잠깐 스트레칭이나 물 한잔으로 깨어나세요! 💧",
        "활기 😎": "에너지 넘치니 친구와 즐거운 활동 해보세요! 🎉"
    }[mood]

    # 결과 카드
    st.markdown(
        f"""
        <div class="card" style="background-color: {card_color};">
            <h2>오늘의 컨디션 {emoji}</h2>
            <p><b>수면 시간:</b> {sleep_hours:.1f}시간</p>
            <p><b>수면 메시지:</b> {sleep_msg}</p>
            <p><b>기분 메시지:</b> {mood_msg}</p>
        </div>
        """, unsafe_allow_html=True
    )
