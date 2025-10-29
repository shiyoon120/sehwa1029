import streamlit as st

# ---- 앱 초기 설정 ----
st.set_page_config(page_title="맞춤 하루 식단 추천", layout="centered")
st.title("🍽️ 맞춤 하루 식단 추천 앱")
st.write("안녕하세요! 먼저 알러지, 복용 약, 질병 정보를 입력해주세요.")

# ---- 사용자 정보 입력 ----
st.header("1️⃣ 기본 정보 입력")
allergies = st.text_input("알러지 정보 (예: 견과류, 유제품)")
medications = st.text_input("복용 약물")
health_conditions = st.text_input("건강 상태/질병")

st.header("2️⃣ 오늘 하루 컨디션 입력")
condition = st.selectbox("오늘 나의 상태를 선택해주세요",
                         ["보통", "피곤함", "체중 감량 필요", "운동 후 회복 필요"])

# ---- 맞춤 식단 추천 ----
st.header("3️⃣ 오늘 하루 맞춤 식단")

# 예시 식단 데이터 (실제 앱에서는 DB 또는 API 연동 가능)
sample_diet = {
    "보통": {
        "아침": ["오트밀 + 바나나", "그릭 요거트", "아몬드 5알"],
        "점심": ["현미밥 + 닭가슴살 + 채소", "사과"],
        "저녁": ["연어구이 + 채소 샐러드", "블루베리"]
    },
    "피곤함": {
        "아침": ["바나나 스무디", "삶은 달걀 2개", "호두 5알"],
        "점심": ["현미밥 + 연어 + 채소", "오렌지"],
        "저녁": ["두부 샐러드 + 렌틸콩", "키위"]
    },
    "체중 감량 필요": {
        "아침": ["그린 스무디", "삶은 달걀 1개", "아몬드 5알"],
        "점심": ["닭가슴살 샐러드", "오이 + 토마토"],
        "저녁": ["두부 + 채소 볶음", "블루베리"]
    },
    "운동 후 회복 필요": {
        "아침": ["바나나 + 오트밀", "삶은 달걀 2개", "호두 5알"],
        "점심": ["현미밥 + 연어 + 시금치", "사과"],
        "저녁": ["닭가슴살 + 채소 샐러드", "키위"]
    }
}

# 추천 식단 가져오기
today_diet = sample_diet.get(condition, sample_diet["보통"])

# ---- 식단 표시 + 주의 음식 체크 ----
for meal, foods in today_diet.items():
    st.subheader(f"🍴 {meal}")
    for food in foods:
        # 알러지 체크
        if allergens := allergies.lower().split(","):
            if any(a.strip() in food.lower() for a in allergens):
                st.markdown(f"⚠️ **{food}** (알러지 주의!)")
                continue
        st.write(f"- {food}")

# ---- 추가 정보 버튼 ----
st.header("4️⃣ 과학적 설명 보기")
if st.button("자세히 보기"):
    st.subheader("🧬 생명과학 관점")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Immune_system_diagram_ko.svg/640px-Immune_system_diagram_ko.svg.png", caption="알러지 반응 예시")
    st.write("""
    - 알러지 유발 성분이 몸에 들어오면 면역세포가 인식하고 히스타민 등을 방출합니다.
    - 이로 인해 피부 발진, 호흡기 반응, 소화기 문제 등이 발생할 수 있습니다.
    """)

    st.subheader("⚗️ 화학적 관점")
    st.write("""
    - 첨가물, 보존제, 산화 가능 물질 등은 특정 조건에서 신체에 영향을 줄 수 있습니다.
    - 예: 방부제 A는 산화 시 위 점막을 자극할 수 있습니다.
    - 섭취량과 농도에 따라 위험도가 달라지므로 주의가 필요합니다.
    """)

st.success("✅ 오늘 하루 맞춤 식단이 준비되었습니다. 건강한 하루 보내세요!")
