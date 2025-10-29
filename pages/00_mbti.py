import streamlit as st
import random

# -----------------------------
# MBTI 근거 기반 노래 데이터
# -----------------------------
mbti_songs = {
    "INTJ": ["Numb - Linkin Park", "Time - Hans Zimmer", "Mad World - Gary Jules"],
    "INTP": ["Stressed Out - Twenty One Pilots", "Lost Stars - Adam Levine", "Breathe Me - Sia"],
    "ENTJ": ["Power - Kanye West", "Eye of the Tiger - Survivor", "Stronger - Kelly Clarkson"],
    "ENTP": ["Thunder - Imagine Dragons", "Blinding Lights - The Weeknd", "Counting Stars - OneRepublic"],
    "INFJ": ["Fix You - Coldplay", "Someone Like You - Adele", "Let Her Go - Passenger"],
    "INFP": ["River Flows in You - Yiruma", "All I Want - Kodaline", "Let It Go - James Bay"],
    "ENFJ": ["We Are Young - Fun.", "What Makes You Beautiful - One Direction", "Beautiful People - Ed Sheeran"],
    "ENFP": ["Happy - Pharrell Williams", "Shake It Off - Taylor Swift", "Good Time - Owl City & Carly Rae Jepsen"],
    "ISTJ": ["Radioactive - Imagine Dragons", "Counting Stars - OneRepublic", "Believer - Imagine Dragons"],
    "ISFJ": ["Perfect - Ed Sheeran", "Photograph - Ed Sheeran", "You Are the Reason - Calum Scott"],
    "ESTJ": ["Fight Song - Rachel Platten", "Eye of the Tiger - Survivor", "Stronger - Kelly Clarkson"],
    "ESFJ": ["Roar - Katy Perry", "Best Day of My Life - American Authors", "Brave - Sara Bareilles"],
    "ISTP": ["Take Me to Church - Hozier", "Believer - Imagine Dragons", "Demons - Imagine Dragons"],
    "ISFP": ["Say You Won’t Let Go - James Arthur", "Before You Go - Lewis Capaldi", "Let Me Down Slowly - Alec Benjamin"],
    "ESTP": ["Can’t Stop the Feeling - Justin Timberlake", "Uptown Funk - Bruno Mars", "On Top of the World - Imagine Dragons"],
    "ESFP": ["Dance Monkey - Tones and I", "Shut Up and Dance - Walk The Moon", "Levitating - Dua Lipa"]
}

# -----------------------------
# Streamlit 앱
# -----------------------------
st.set_page_config(page_title="MBTI 노래 추천기", layout="centered")
st.title("🎧 MBTI 기반 근거 있는 노래 추천기")

user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", ["선택하세요"] + list(mbti_songs.keys()))

if st.button("추천받기 🎵"):
    if user_mbti in mbti_songs:
        songs = random.sample(mbti_songs[user_mbti], 3)
        st.success(f"🎶 {user_mbti}에게 어울리는 추천곡 🎶")
        for idx, song in enumerate(songs, start=1):
            st.write(f"{idx}. {song}")
        st.balloons()
    else:
        st.warning("⚠️ MBTI를 선택해주세요!")
