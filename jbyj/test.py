import streamlit as st

st.title("🔢 MBTI 점수 입력 테스트")
st.write("각 질문에 대해 본인의 생각을 1~5 사이 숫자로 입력해주세요.!")

questions = [
    ("나는 사람들과 함께 있을 때 에너지가 생긴다", "E"),
    ("혼자 있는 시간이 필요하다", "I"),
    ("사실보다는 아이디어가 더 중요하다", "N"),
    ("현실적이고 구체적인 것이 좋다", "S"),
    ("논리적으로 생각하고 판단한다", "T"),
    ("감정과 분위기를 중시한다", "F"),
    ("계획적인 것을 선호한다", "J"),
    ("즉흥적이고 유연한 편이다", "P"),
]

scores = {
    "E": 0,
    "I": 0,
    "S": 0,
    "N": 0,
    "T": 0,
    "F": 0,
    "J": 0,
    "P": 0,
}

st.subheader("📝 점수를 입력하세요 (1 ~ 5)")
for i, (question, mbti_type) in enumerate(questions):
    score = st.number_input(f"{i+1}. {question}", min_value=1, max_value=5, value=3, step=1)
    scores[mbti_type] += score

if st.button("결과 분석"):
    ei = "E" if scores["E"] >= scores["I"] else "I"
    sn = "S" if scores["S"] >= scores["N"] else "N"
    tf = "T" if scores["T"] >= scores["F"] else "F"
    jp = "J" if scores["J"] >= scores["P"] else "P"

    result = ei + sn + tf + jp

    st.success(f"당신의 예측한 MBTI 유형은 **{result}** 입니다!")