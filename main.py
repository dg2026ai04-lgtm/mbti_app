import streamlit as st
st.title('나만의 MBTI 앱!')
st.write('여기에 무엇을 넣어볼까요?!')
import streamlit as st

st.set_page_config(
    page_title="MBTI 청소년 도서 추천",
    page_icon="📚"
)

st.title("📚 MBTI 기반 청소년 문학 추천")
st.write("당신의 MBTI를 선택하면 어울리는 청소년 문학을 추천해드립니다! ✨")

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

books = {
    "INTJ": ("📖 어린 왕자", "깊은 철학과 통찰을 좋아하는 INTJ에게 추천"),
    "INTP": ("📖 멋진 신세계", "생각할 거리를 던지는 작품"),
    "ENTJ": ("📖 해리 포터", "목표지향적인 ENTJ에게 어울리는 성장 이야기"),
    "ENTP": ("📖 이상한 나라의 앨리스", "창의적이고 상상력 넘치는 ENTP에게"),
    "INFJ": ("📖 모모", "세상을 깊이 바라보는 INFJ에게"),
    "INFP": ("📖 나니아 연대기", "상상력과 감성이 풍부한 INFP에게"),
    "ENFJ": ("📖 작은 아씨들", "사람과 관계를 중시하는 ENFJ에게"),
    "ENFP": ("📖 빨강머리 앤", "열정과 에너지가 넘치는 ENFP에게"),
    "ISTJ": ("📖 로빈슨 크루소", "성실하고 현실적인 ISTJ에게"),
    "ISFJ": ("📖 플랜더스의 개", "따뜻한 마음의 ISFJ에게"),
    "ESTJ": ("📖 톰 소여의 모험", "활동적이고 리더십 있는 ESTJ에게"),
    "ESFJ": ("📖 비밀의 화원", "사람을 좋아하는 ESFJ에게"),
    "ISTP": ("📖 80일간의 세계일주", "모험을 좋아하는 ISTP에게"),
    "ISFP": ("📖 별", "감성적인 ISFP에게"),
    "ESTP": ("📖 보물섬", "스릴을 좋아하는 ESTP에게"),
    "ESFP": ("📖 피터 팬", "즐거움을 추구하는 ESFP에게")
}

if st.button("📚 책 추천 받기"):
    title, desc = books[mbti]

    st.success(f"✨ {mbti}에게 추천하는 책!")

    st.write("###", title)
    st.write(desc)

    st.balloons()

    st.write("💡 오늘의 독서 Tip")
    st.info("하루 20분만 읽어도 독서 습관이 생깁니다!")
