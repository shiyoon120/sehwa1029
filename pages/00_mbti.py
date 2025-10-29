import streamlit as st
import random

# -----------------------------
# MBTI 데이터 (근거 기반)
# -----------------------------
mbti_info = {
    "INTJ": {"desc": "전략적, 계획적, 자기 주도형", "color": "#D0E1F9", "mood": "calm", "songs": [
        {"title": "Numb - Linkin Park", "genre": "Rock", "emoji": "🎸"},
        {"title": "Time - Hans Zimmer", "genre": "Instrumental", "emoji": "⏳"},
        {"title": "Mad World - Gary Jules", "genre": "Pop", "emoji": "🌙"}
    ]},
    "INFP": {"desc": "이상주의적, 감성적, 내향적", "color": "#F9D0D0", "mood": "sad", "songs": [
        {"title": "River Flows in You - Yiruma", "genre": "Instrumental", "emoji": "🎹"},
        {"title": "All I Want - Kodaline", "genre": "Pop", "emoji": "💔"},
        {"title": "Let It Go - James Bay", "genre": "Pop", "emoji": "❄️"}
    ]},
    "ENFP": {"desc": "자유로운 영혼, 활발, 창의적", "color": "#FFF3D0", "mood": "happy", "songs": [
        {"title": "Happy - Pharrell Williams", "genre": "Pop", "emoji": "🌞"},
        {"title": "Shake It Off - Taylor Swift", "genre": "Pop", "emoji": "💃"},
        {"title": "Good Time - Owl City & Carly Rae Jepsen", "genre": "Pop", "emoji": "🎉"}
    ]},
    # ... 나머지 MBTI도 같은 구조로 추가 가능
}

mood_colors = {
    "happy": "#FFF9C4",
    "sad": "#B3E5FC",
    "calm": "#DCE775",
    "energetic": "#FFCC80"
}

# -----------------------------
# Streamlit 앱 설정
# -----------------------------
st.set_page_config(page_title="🎧 MBTI 감성 음악 추천기", layout="centered")
st.title("🎧 MBTI 감성 음악 추천기")
st.write("당신의 MBTI와 오늘 기분을 입력하면, 맞춤형 음악을 추천해드려요 💫")

# -----------------------------
# 사용자 입력
# -----------------------------
user_mbti = st.selectbox("1️⃣ MBTI 선택", ["선택하세요"] + list(mbti_info.keys()))
user_mood = st.selectbox("2️⃣ 오늘 기분 선택", ["선택하세요", "happy", "sad", "calm", "energetic"])

# -----------------------------
# 추천곡 표시 함수
# -----------------------------
def show_songs(mbti_key, mood_filter=None):
    info = mbti_info[mbti_key]
    
    # MBTI 테마 색상 적용
    st.markdown(f"<div style='background-color:{info['color']};padding:15px;border-radius:10px'>", unsafe_allow_html=True)
    st.subheader(f"{mbti_key} - {info['desc']}")
    st.markdown("</div>", unsafe_allow_html=True)

    # 곡 선택
    songs_pool = info["songs"]
    if mood_filter:
        # mood 매칭 필터링 (간단하게)
        songs_pool = [s for s in songs_pool if info['mood'] == mood_filter]
        if not songs_pool:  # 필터 없으면 원래 pool
            songs_pool = info["songs"]

    songs = random.sample(songs_pool, min(3, len(songs_pool)))

    # 카드 형태로 표시
    for s in songs:
        st.markdown(f"**{s['emoji']} {s['title']}**  _(장르: {s['genre']})_")

# -----------------------------
# 버튼 클릭 시 추천
# -----------------------------
if st.button("3️⃣ 추천곡 보기 🎵"):
    if user_mbti in mbti_info and user_mood in mood_colors:
        show_songs(user_mbti, user_mood)
        st.balloons()
    else:
        st.warning("⚠️ MBTI와 오늘 기분을 모두 선택해주세요!")

# -----------------------------
# "다른 추천곡 보기" 버튼
# -----------------------------
if st.button("🔁 다른 추천곡 보기"):
    if user_mbti in mbti_info and user_mood in mood_colors:
        show_songs(user_mbti, user_mood)
    else:
        st.warning("⚠️ MBTI와 오늘 기분을 먼저 선택해주세요!")
