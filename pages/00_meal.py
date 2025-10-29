import streamlit as st
from PIL import Image

# ---- 1️⃣ 세션 상태 초기화 ----
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'show_info' not in st.session_state:
    st.session_state.show_info = False

st.set_page_config(page_title="맞춤 하루 식단", layout="centered")
st.title("🍽️ 맞춤 하루 식단 추천 앱")
st.write("자유롭게 알러지, 복용 약, 질병, 하루 컨디션 입력 후 '입력 완료' 버튼을 눌러주세요.")

# ---- 2️⃣ 사용자 자유 입력 ----
allergies = st.text_input("알러지 정보 (예: 견과류, 유제품)", "")
medications = st.text_input("복용 약물", "")
health_conditions = st.text_input("건강 상태/질병", "")
condition = st.text_input("오늘 하루 컨디션 (예: 피곤하다, 체중 조절 필요 등)", "")

# ---- 3️⃣ 입력 완료 버튼 ----
if st.button("입력 완료"):
    st.session_state.submitted = True

# ---- 4️⃣ 식단 예시 데이터 ----
sample_diet = {
    "보통": {"아침": ["oatmeal","banana","almond"], "점심": ["rice","chicken","vegetables"], "저녁": ["salmon","salad","blueberry"]},
    "피곤": {"아침": ["banana_smoothie","egg","walnut"], "점심": ["rice","salmon","vegetables"], "저녁": ["tofu_salad","lentils","kiwi"]},
    "체중": {"아침": ["green_smoothie","egg","almond"], "점심": ["chicken_salad","cucumber","tomato"], "저녁": ["tofu","stir_vegetables","blueberry"]},
    "운동": {"아침": ["banana","oatmeal","egg"], "점심": ["rice","salmon","spinach"], "저녁": ["chicken","salad","kiwi"]}
}

# ---- 5️⃣ 입력 완료 후 하루 식단 표시 ----
if st.session_state.submitted:
    # 키워드 기반 식단 추천
    key = "보통"
    condition_lower = condition.lower()
    if "피곤" in condition_lower:
        key = "피곤"
    elif "체중" in condition_lower:
        key = "체중"
    elif "운동" in condition_lower or "회복" in condition_lower:
        key = "운동"

    today_diet = sample_diet[key]

    st.header("🍴 오늘 하루 맞춤 식단")
    allergens_list = [a.strip().lower() for a in allergies.split(",")] if allergies else []

    for meal, foods in today_diet.items():
        st.subheader(f"{meal}")
        display_foods = []
        for food in foods:
            if any(a in food.lower() for a in allergens_list):
                display_foods.append(f"⚠️ {food}")
            else:
                display_foods.append(food)
        st.write(display_foods)

        # ---- 식판 그림 ----
        plate = Image.new("RGBA", (300, 100), (255, 255, 240, 255))
        x_offset = 10
        for food in foods:
            try:
                icon = Image.open(f"icons/{food}.png").resize((60,60))  # icons 폴더에 음식 PNG 필요
                plate.paste(icon, (x_offset, 20), icon)
            except:
                # 아이콘 없으면 사각형으로 대체
                from PIL import ImageDraw
                draw = ImageDraw.Draw(plate)
                color = (255,0,0) if any(a in food.lower() for a in allergens_list) else (0,128,0)
                draw.rectangle([x_offset,20,x_offset+60,80], fill=color)
            x_offset += 70
        st.image(plate, caption=f"{meal} 식판 그림")

    # ---- 6️⃣ 추가 설명 버튼 ----
    if st.button("추가 설명 보기"):
        st.session_state.show_info = True

    if st.session_state.show_info:
        st.subheader("🧬 생명과학 관점")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Immune_system_diagram_ko.svg/640px-Immune_system_diagram_ko.svg.png", caption="알러지 반응 예시")
        st.write("""
        - 알러지 유발 성분이 몸에 들어오면 면역세포가 인식하고 히스타민 등을 방출합니다.
        - 피부 발진, 호흡기 반응, 소화기 문제 등이 발생할 수 있습니다.
        """)

        st.subheader("⚗️ 화학적 관점")
        st.write("""
        - 첨가물, 보존제, 산화 가능 물질 등은 특정 조건에서 신체에 영향을 줄 수 있습니다.
        - 예: 방부제 A는 산화 시 위 점막을 자극할 수 있습니다.
        - 섭취량과 농도에 따라 위험도가 달라지므로 주의가 필요합니다.
        """)

    st.success("✅ 오늘 하루 맞춤 식단이 준비되었습니다. 건강한 하루 보내세요!")
