import streamlit as st
import random

# -----------------------------
# MBTI 데이터
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
    "ISFJ": {"desc": "헌신적, 감성, 안
