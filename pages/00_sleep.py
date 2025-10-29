import streamlit as st
from datetime import datetime, timedelta

st.title("🌙 나만의 수면 분석기 🌞")
st.write("수면 시작과 기상 시간을 입력하면 오늘 나의 컨디션을 알려드려요!")

# 입력
sleep_time = st.time_input("💤 오늘 잠든 시간", value=datetime.strptime("22:30", "%H:%M").time())
wake_time = st.time_input("⏰ 오늘 기상 시간", value=datetime.strptime("07:30", "%H:%M").time())
mood = st.selectbox("오늘 기분 선택", ["좋음 😄", "보통 😐", "졸림 😴", "활기 😎"])

if st.button("📝 컨디션 확인"):
    # 시간 계산
    sleep_dt = datetime.combine(datetime.today(), sleep_time)
    wake_dt = datetime.combine(datetime.today(), wake_time)
    if wake_dt <= sleep_dt:  # 다음날로 넘어가는 경우
        wake_dt += timedelta(days=1)
    sleep_hours = (wake_dt - sleep_dt).seconds / 3600
    
    # 컨디션 메시지
    if sleep_hours >= 8:
        sleep_msg = "푹 잤네요! 오늘 하루 활기차게 보내세요! 🌞"
        color = "💛"
    elif 6 <= sleep_hours < 8:
        sleep_msg = "충분히 잤지만 조금 피곤할 수 있어요. ☁️"
        color = "💙"
    else:
        sleep_msg = "조금 부족한 잠! 오늘은 무리하지 말고 쉬세요. 💤"
        color = "💜"
    
    # 사용자 선택과 합치기
    mood_msg = ""
    if mood == "좋음 😄":
        mood_msg = "기분 좋으니 오늘은 새로운 걸 도전해보세요! ✨"
    elif mood == "보통 😐":
        mood_msg = "평온하게, 일상의 루틴을 지켜보세요. 🛋️"
    elif mood == "졸림 😴":
        mood_msg = "잠깐 스트레칭이나 물 한잔으로 깨어나세요! 💧"
    else:  # 활기 😎
        mood_msg = "에너지 넘치니 친구와 즐거운 활동 해보세요! 🎉"
    
    st.markdown(f"### 🌈 오늘의 컨디션")
    st.markdown(f"**수면 시간:** {sleep_hours:.1f}시간 {color}")
    st.markdown(f"**수면 메시지:** {sleep_msg}")
    st.markdown(f"**기분 메시지:** {mood_msg}")
