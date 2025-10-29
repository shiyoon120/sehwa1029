import streamlit as st
import random

# MBTI 데이터
mbti_info = {
    "INTJ": ["Numb - Linkin Park 🎸", "Time - Hans Zimmer ⏳", "Mad World - Gary Jules 🌙"],
    "INTP": ["Stressed Out - Twenty One Pilots 🌀", "Lost Stars - Adam Levine 🌟", "Breathe Me - Sia 😶‍🌫️"],
    "ENTJ": ["Power - Kanye West 💪", "Eye of the Tiger - Survivor 🐅", "Stronger - Kelly Clarkson ⚡"],
    "ENTP": ["Thunder - Imagine Dragons ⚡", "Blinding Lights - The Weeknd 🌃", "Counting Stars - OneRepublic ⭐"],
    "INFJ": ["Fix You - Coldplay 🕯️", "Someone Like You - Adele 💔", "Let Her Go - Passenger 🌧️"],
    "INFP": ["River Flows in You - Yiruma 🎹", "All I Want - Kodaline 💔", "Let It Go - James Bay ❄️"],
    "ENFJ": ["We Are Young - Fun. 🎉", "What Makes You Beautiful - One Direction 💖", "Beautiful People - Ed Sheeran 🌟"],
    "ENFP": ["Happy - Pharrell Williams 🌞", "Shake It Off - Taylor Swift 💃", "Good Time - Owl City & Carly Rae Jepsen 🎊"],
    "ISTJ": ["Radioactive - Imagine Dragons ⚡", "Counting Stars - OneRepublic ⭐", "Believer - Imagine Dragons 🔥"],
    "ISFJ": ["Perfect - Ed Sheeran 💖", "Photograph - Ed Sheeran 📸", "You Are the Reason - Calum Scott ❤️"],
    "ESTJ": ["Fight Song - Rachel Platten ⚡", "Eye of the Tiger - Survivor 🐅", "Stronger - Kelly Clarkson 💪"],
    "ESFJ": ["Roar - Katy Perry 🦁", "Best Day of My Life - American Authors 🎉", "Brave - Sara Bareilles 🛡️"],
    "ISTP": ["Take Me to Church - Hozier ⛪", "Believer - Imagine Dragons 🔥", "Demons - Imagine Dragons 😈"],
    "ISFP": ["Say You Won’t Let Go - James Arthur ❤️", "Before You Go - Lewis Capaldi 😢", "Let Me Down Slowly - Alec Benjamin 💔"],
    "ESTP": ["Can’t Stop the Feeling - Justin Timberlake 💃", "Uptown Funk - Bruno Mars 🎷", "On Top of the World - Imagine Dragons 🌍"],
    "ESFP": ["Dance Monkey - Tones and I 🐒", "Shut Up and Dance - Walk The Moon 💃", "Levitating - Dua Lipa 🪩"]
}

st.title("🎧 MBTI 음악 추천기")
st.write("당신의 MBTI를 선택하면, 어울리는 음악을 추천해드립니다!")

# MBTI 선택
user_mbti = st.selectbox("MBTI 선택", ["선택하세요"] + list(mbti_info.keys()))

if st.button("추천곡 보기"):
    if user_mbti in mbti_info:
        songs = random.sample(mbti_info[user_mbti], 3)
        st.write(f"🎵 {user_mbti}님을 위한 추천곡:")
        for s in songs:
            st.write(s)
        st.balloons()
    else:
        st.warning("MBTI를 선택해주세요!")
