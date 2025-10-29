import streamlit as st
import random

# -----------------------------
# MBTI 근거 데이터 (16개 전부)
# -----------------------------
mbti_info = {
    "INTJ": {"desc": "전략적, 계획적, 자기 주도형", "color": "#D0E1F9", "mood": "calm", "songs": [
        {"title": "Numb - Linkin Park", "genre": "Rock", "emoji": "🎸"},
        {"title": "Time - Hans Zimmer", "genre": "Instrumental", "emoji": "⏳"},
        {"title": "Mad World - Gary Jules", "genre": "Pop", "emoji": "🌙"}
    ]},
    "INTP": {"desc": "분석적, 호기심 많고 내향적", "color": "#DCE775", "mood": "calm", "songs": [
        {"title": "Stressed Out - Twenty One Pilots", "genre": "Pop/Rock", "emoji": "🌀"},
        {"title": "Lost Stars - Adam Levine", "genre": "Pop", "emoji": "🌟"},
        {"title": "Breathe Me - Sia", "genre": "Pop", "emoji": "😶‍🌫️"}
    ]},
    "ENTJ": {"desc": "리더형, 외향적, 목표 지향", "color": "#FFCC80", "mood": "energetic", "songs": [
        {"title": "Power - Kanye West", "genre": "Hip-Hop", "emoji": "💪"},
        {"title": "Eye of the Tiger - Survivor", "genre": "Rock", "emoji": "🐅"},
        {"title": "Stronger - Kelly Clarkson", "genre": "Pop", "emoji": "⚡"}
    ]},
    "ENTP": {"desc": "창의적, 즉흥적, 활발", "color": "#FFECB3", "mood": "energetic", "songs": [
        {"title": "Thunder - Imagine Dragons", "genre": "Rock", "emoji": "⚡"},
        {"title": "Blinding Lights - The Weeknd", "genre": "Pop", "emoji": "🌃"},
        {"title": "Counting Stars - OneRepublic", "genre": "Pop", "emoji": "⭐"}
    ]},
    "INFJ": {"desc": "통찰력, 내향적, 감성적", "color": "#F8BBD0", "mood": "calm", "songs": [
        {"title": "Fix You - Coldplay", "genre": "Pop", "emoji": "🕯️"},
        {"title": "Someone Like You - Adele", "genre": "Pop", "emoji": "💔"},
        {"title": "Let Her Go - Passenger", "genre": "Pop", "emoji": "🌧️"}
    ]},
    "INFP": {"desc": "이상주의적, 감성적, 내향적", "color": "#F9D0D0", "mood": "sad", "songs": [
        {"title": "River Flows in You - Yiruma", "genre": "Instrumental", "emoji": "🎹"},
        {"title": "All I Want - Kodaline", "genre": "Pop", "emoji": "💔"},
        {"title": "Let It Go - James Bay", "genre": "Pop", "emoji": "❄️"}
    ]},
    "ENFJ": {"desc": "외향적, 감정 이입, 리더십", "color": "#FFE0B2", "mood": "happy", "songs": [
        {"title": "We Are Young - Fun.", "genre": "Pop", "emoji": "🎉"},
        {"title": "What Makes You Beautiful - One Direction", "genre": "Pop", "emoji": "💖"},
        {"title": "Beautiful People - Ed Sheeran", "genre": "Pop", "emoji": "🌟"}
    ]},
    "ENFP": {"desc": "자유로운 영혼, 활발, 창의적", "color": "#FFF3D0", "mood": "happy", "songs": [
        {"title": "Happy - Pharrell Williams", "genre": "Pop", "emoji": "🌞"},
        {"title": "Shake It Off - Taylor Swift", "genre": "Pop", "emoji": "💃"},
        {"title": "Good Time - Owl City & Carly Rae Jepsen", "genre": "Pop", "emoji": "🎊"}
    ]},
    "ISTJ": {"desc": "현실적, 계획적, 신중", "color": "#C8E6C9", "mood": "calm", "songs": [
        {"title": "Radioactive - Imagine Dragons", "genre": "Rock", "emoji": "⚡"},
        {"title": "Counting Stars - OneRepublic", "genre": "Pop", "emoji": "⭐"},
        {"title": "Believer - Imagine Dragons", "genre": "Rock", "emoji": "🔥"}
    ]},
    "ISFJ": {"desc": "헌신적, 감성, 안정적", "color": "#FFCCBC", "mood": "calm", "songs": [
        {"title": "Perfect - Ed Sheeran", "genre": "Pop", "emoji": "💖"},
        {"title": "Photograph - Ed Sheeran", "genre": "Pop", "emoji": "📸"},
        {"title": "You Are the Reason - Calum Scott", "genre": "Pop", "emoji": "❤️"}
    ]},
    "ESTJ": {"desc": "외향적, 조직적, 현실적", "color": "#FFE082", "mood": "energetic", "songs": [
        {"title": "Fight Song - Rachel Platten", "genre": "Pop", "emoji": "⚡"},
        {"title": "Eye of the Tiger - Survivor", "genre": "Rock", "emoji": "🐅"},
        {"title": "Stronger - Kelly Clarkson", "genre": "Pop", "emoji": "💪"}
    ]},
    "ESFJ": {"desc": "사교적, 감성적, 친절", "color": "#FFAB91", "mood": "happy", "songs": [
        {"title": "Roar - Katy Perry", "genre": "Pop", "emoji": "🦁"},
        {"title": "Best Day of My Life - American Authors", "genre": "Pop", "emoji": "🎉"},
        {"title": "Brave - Sara Bareilles", "genre": "Pop", "emoji": "🛡️"}
    ]},
    "ISTP": {"desc": "모험적, 분석적, 자유로운", "color": "#B2DFDB", "mood": "energetic", "songs": [
        {"title": "Take Me to Church - Hozier", "genre": "Pop/Rock", "emoji": "⛪"},
        {"title": "Believer - Imagine Dragons", "genre": "Rock", "emoji": "🔥"},
        {"title": "Demons - Imagine Dragons", "genre": "Rock", "emoji": "😈"}
    ]},
    "ISFP": {"desc": "예술적, 감성, 즉흥적", "color": "#F48FB1", "mood": "sad", "songs": [
        {"title": "Say You Won’t Let Go - James Arthur", "genre": "Pop", "emoji": "❤️"},
        {"title": "Before You Go - Lewis Capaldi", "genre": "Pop", "emoji": "😢"},
        {"title": "Let Me Down Slowly - Alec Benjamin", "genre": "Pop", "emoji": "💔"}
    ]},
    "ESTP": {"desc": "외향적, 모험적, 에너지 넘침", "color": "#FFD54F", "mood": "energetic", "songs": [
        {"title": "Can’t Stop the Feeling - Justin Timberlake", "genre": "Pop", "emoji": "💃"},
        {"title": "Uptown Funk - Bruno Mars", "genre": "Funk/Pop", "emoji": "🎷"},
        {"title": "On Top of the World - Imagine Dragons", "genre": "Pop/Rock", "emoji": "🌍"}
    ]},
    "ESFP": {"desc": "사교적, 즐거움 추구, 활발", "color": "#FF8A65", "mood": "happy", "songs": [
        {"title": "Dance Monkey - Tones and I", "genre": "Pop", "emoji": "🐒"},
        {"title": "Shut Up and Dance - Walk The Moon", "genre": "Pop/Rock", "emoji": "💃"},
        {"title": "Levitating - Dua Lipa", "genre": "Pop", "emoji": "🪩"}
    ]}
}

# -----------------------------
# Streamlit 앱
# -----------------------------
st.set_page_config(page_title="🎧 MBTI 감성 음악 추천기", layout="centered")
st.title("🎧 16개 MBTI 기반 인터랙티브 음악 추천기")
st.write("당신의 MBTI와 오늘 기분을 입력하면, 맞춤형 음악을 추천해드려요 💫")

# -----------------------------
# 사용자 입력
# -----------------------------
user_mbti = st.selectbox("1️⃣ MBTI 선택", ["선택하세요"] + list(mbti_info.keys()))
user_mood = st.selectbox("2️⃣ 오늘 기분 선택", ["선택하세요", "happy", "sad", "calm", "energetic"])

# -----------------------------
# 추천곡 표시 함수
# -----------------------------
def show_s
