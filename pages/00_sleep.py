import streamlit as st
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="🌙 수면 분석기", page_icon="🛌", layout="wide")

# 배경 스타일
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #E0F7FA, #FFFDE7);
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .card h2 {
        margin-top: 0;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌙 나만의 수면 분석기")
st.write("수면 시작과 기상 시간을 입력하면 오늘 컨디션과 추천 메시지를 알려드려요!")

# 입력
col1, col2 = st.columns(2)
with col1:
    sleep_time = st.time_input("💤 잠든 시간", value=datetime.strptime("23:00", "%H:%M").time())
    wake_time = st.time_input("⏰ 기상 시간", value=datetime.strptime("07:30", "%H:%M").time())
with col2:
    mood = st.selectbox("오늘 기분 선택", ["좋음 😄", "보통 😐", "졸림 😴", "활기 😎"])

if st.button("📝 컨디션 확인"):
    # 시간 계산
    sleep_dt = datetime.combine(datetime.today(), sleep_time)
    wake_dt = datetime.combine(datetime.today(), wake_time)
    if wake_dt <= sleep_dt:
        wake_dt += timedelta(days=1)
    sleep_hours = (wake_dt - sleep_dt).seconds / 3600

    # 수면 상태
    if sleep_hours >= 8:
        sleep_msg = "푹 잤네요! 오늘 하루 활기차게 보내세요! 🌞"
        sleep_color = "#A8E6CF"  # 연한 초록
        sleep_emoji = "☀️"
    elif 6 <= sleep_hours < 8:
        sleep_msg = "충분히 잤지만 조금 피곤할 수 있어요. ☁️"
        sleep_color = "#FFD3B6"  # 연한 주황
        sleep_emoji = "🌤️"
    else:
        sleep_msg = "조금 부족한 잠! 오늘은 무리하지 말고 쉬세요. 💤"
        sleep_color = "#FFAAA5"  # 연한 빨강
        sleep_emoji = "🌙"

    # 기분 메시지
    mood_messages = {
        "좋음 😄": "기분 좋으니 오늘은 새로운 걸 도전해보세요! ✨",
        "보통 😐": "평온하게, 일상의 루틴을 지켜보세요. 🛋️",
        "졸림 😴": "잠깐 스트레칭이나 물 한잔으로 깨어나세요! 💧",
        "활기 😎": "에너지 넘치니 친구와 즐거운 활동 해보세요! 🎉"
    }
    mood_msg = mood_messages[mood]
    mood_color = "#DCE775"  # 연한 노랑
    mood_emoji = mood.split()[1]

    # 카드 레이아웃
    card_html = f"""
    <div style="display:flex; gap:20px;">
        <div class="card" style="background-color:{sleep_color}; flex:1;">
            <h2>수면 정보 {sleep_emoji}</h2>
            <p><b>잠든 시간:</b> {sleep_time.strftime('%H:%M')}</p>
            <p><b>기상 시간:</b> {wake_time.strftime('%H:%M')}</p>
            <p><b>총 수면 시간:</b> {sleep_hours:.1f}시간</p>
            <p>{sleep_msg}</p>
        </div>
        <div class="card" style="background-color:{mood_color}; flex:1;">
            <h2>오늘 기분 {mood_emoji}</h2>
            <p>{mood_msg}</p>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
