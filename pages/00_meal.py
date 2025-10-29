import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="맞춤 하루 식단", layout="centered")
st.title("🍽️ 맞춤 하루 식단 추천 앱")
st.write("안녕하세요! 알러지, 복용 약, 건강 상태, 하루 컨디션 정보를 입력해주세요.")

# ---- 1️⃣ 사용자 정보 입력 ----
st.header("기본 정보 입력")
allergies = st.text_input("알러지 정보 (예: 견과류, 유제품)")
medications = st.text_input("복용 약물")
health_conditions = st.text_input("건강 상태/질병")

st.header("오늘 하루 컨디션")
condition = st.selectbox("오늘 나의 상태를 선택해주세요",
                         ["보통", "피곤함", "체중 감량 필요", "운동 후 회복 필요"])

# ---- 2️⃣ 맞춤 식단 ----
st.header("오늘 하루 맞춤 식단")
sample_diet = {
    "보통": {"아침": ["오트밀", "바나나", "아몬드"], "점심": ["현미밥", "닭가슴살", "채소"], "저녁": ["연어", "채소 샐러드", "블루베리"]},
    "피곤함": {"아침": ["바나나 스무디", "삶은 달걀", "호두"], "점심": ["현미밥", "연어", "채소"], "저녁": ["두부 샐러드", "렌틸콩", "키위"]},
    "체중 감량 필요": {"아침": ["그린 스무디", "삶은 달걀", "아몬드"], "점심": ["닭가슴살 샐러드", "오이", "토마토"], "저녁": ["두부", "채소 볶음", "블루베리"]},
    "운동 후 회복 필요": {"아침": ["바나나", "오트밀", "삶은 달걀"], "점심": ["현미밥", "연어", "시금치"], "저녁": ["닭가슴살", "채소 샐러드", "키위"]}
}

today_diet = sample_diet.get(condition, sample_diet["보통"])

# ---- 3️⃣ 식판 그림 생성 ----
def create_plate_image(foods, allergens=[]):
    # 식판 배경
    plate = Image.new("RGB", (300, 100), color=(255, 255, 240))
    draw = ImageDraw.Draw(plate)
    # 글꼴 설정 (환경에 따라 경로 수정 필요)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except:
        font = ImageFont.load_default()
    # 음식 아이콘 / 텍스트 배치
    x_offset = 10
    for food in foods:
        color = (255, 0, 0) if any(a.strip().lower() in food.lower() for a in allergens) else (0, 128, 0)
        draw.rectangle([x_offset, 20, x_offset+60, 80], fill=color)
        draw.text((x_offset+5, 50), food[:10], fill=(255,255,255), font=font)
        x_offset += 70
    return plate

for meal, foods in today_diet.items():
    st.subheader(f"🍴 {meal}")
    # 알러지 체크
    display_foods = []
    for food in foods:
        if allergies:
            if any(a.strip().lower() in food.lower() for a in allergies.lower().split(",")):
                display_foods.append(f"⚠️ {food}")
            else:
                display_foods.append(food)
        else:
            display_foods.append(food)
    st.write(display_foods)
    plate_img = create_plate_image(foods, allergies.lower().split(",") if allergies else [])
    st.image(plate_img, caption=f"{meal} 식판 그림")

# ---- 4️⃣ 추가 정보 버튼 ----
st.header("과학적 설명")
if st.button("자세히 보기"):
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
