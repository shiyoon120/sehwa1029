import streamlit as st
import random

# -----------------------------
# MBTI별 추천 노래 데이터
# -----------------------------
mbti_songs = {
    "INTJ": ["Lucid Dreams - Juice WRLD", "Numb - Linkin Park", "Night Changes - One Direction"],
    "INTP": ["Stressed Out - Twenty One Pilots", "Lost Stars - Adam Levine", "Yellow - Coldplay"],
    "ENTJ": ["Power - Kanye West", "Can't Hold Us - Macklemore", "Hall of Fame - The Script"],
    "ENTP": ["Thunder - Imagine Dragons", "Counting Stars - OneRepublic", "Blinding Lights - The Weeknd"],
    "INFJ": ["Fix You - Coldplay", "Someone Like You - Adele", "Let Her Go - Passenger"],
    "INFP": ["Little Do You Know - Alex & Sierra", "Let It Go - James Bay", "All I Want - Kodaline"],
    "ENFJ": ["Beautiful People - Ed Sheeran", "We Are Young - Fun.", "What Makes You Beautiful - One Direction"],
    "ENFP": ["Happy - Pharrell Williams", "Shake It Off - Taylor Swift", "Good Time - Owl City & Carly Rae Jepsen"],
    "ISTJ": ["Counting Stars - OneRepublic", "Radioactive - Imagine Dragons", "Believer - Imagine Dragons"],
    "ISFJ": ["Photograph - Ed Sheeran", "You Are the Reason - Calum Scott", "Perfect - Ed Sheeran"],
    "ESTJ": ["Stronger - Kelly Clarkson", "Fight Song - Rachel Platten", "Eye of the Tiger - Survivor"],
    "ESFJ": ["Best Day of My Life - American Authors", "Roar - Katy Perry", "Brave - Sara Bareilles"],
    "ISTP": ["Believer - Imagine Dragons", "Take Me to Church - Hozier", "Demons - Imagine Dragons"],
    "ISFP": ["Say You Won’t Let Go - James Arthur", "Let Me Down Slowly - Alec Benjamin", "Before You Go - Lewis Capaldi"],
    "ESTP": ["Can’t Stop the Feeling - Justin Timberlake", "Uptown Funk - Bruno Mars", "On Top of the World - Imagine Dragons"],
    "ESFP": ["Dance Monkey - Tones and I", "Levitating - Dua Lipa", "Shut Up and Dance - Walk The Moon"]
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="MBTI 노래 추천기", page_icon="🎧", layout="centered")

st.title("🎧 MBTI 기반 노래 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 노래를 추천해드릴게요!")

# MBTI 선택
mbti_list = list(mbti_songs.keys())
user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", ["선택하세요"] + mbti_list)

# 추천 버튼
if st.button("노래 추천받기 🎵"):
    if user_mbti in mbti_songs:
        songs = random.sample(mbti_songs[user_mbti], 3)
        st.success(f"🎶 {user_mbti} 유형에게 어울리는 노래 추천 🎶")
        for idx, song in enumerate(songs, start=1):
            st.write(f"{idx}. {song}")
    else:
        st.warning("⚠️ MBTI를 선택해주세요!")

# 푸터
st.markdown("---")
st.caption("✨ Made with Streamlit | Python 3.10 ✨")
