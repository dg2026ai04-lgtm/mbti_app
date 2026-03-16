import streamlit as st
st.title('나만의 MBTI 앱!')
st.write('여기에 무엇을 넣어볼까요?!')
import streamlit as st

st.set_page_config(
    page_title="MBTI 독서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 기반 청소년 문학 추천")
st.write("당신의 성격 유형에 어울리는 책을 통해 **새로운 생각과 영감**을 얻어보세요 ✨")

st.divider()

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

data = {

"INTJ": {
"desc":"전략적이고 미래지향적인 사고를 하는 사색가형입니다.",
"books":[
("어린 왕자","삶의 본질과 인간 관계를 깊게 생각하게 합니다."),
("멋진 신세계","사회 구조와 인간의 자유에 대해 고민하게 합니다."),
("1984","비판적 사고와 사회 인식을 키워줍니다.")
],
"lesson":"세상을 분석하고 더 나은 미래를 설계하는 힘을 기를 수 있습니다.",
"question":"우리가 사는 사회에서 진정한 자유란 무엇일까요?",
"quote":"중요한 것은 눈에 보이지 않는다."
},

"INFP":{
"desc":"이상과 가치를 중요하게 생각하는 감성적인 이상주의자입니다.",
"books":[
("나니아 연대기","상상력과 도덕적 선택을 생각하게 합니다."),
("모모","시간과 삶의 의미를 고민하게 합니다."),
("빨강머리 앤","자기다움과 꿈을 지키는 이야기입니다.")
],
"lesson":"자신의 가치와 꿈을 지키는 용기를 배울 수 있습니다.",
"question":"나에게 가장 중요한 가치는 무엇일까요?",
"quote":"상상력은 삶을 더 아름답게 만든다."
},

"ENFP":{
"desc":"열정적이고 창의적인 아이디어가 많은 탐험가형입니다.",
"books":[
("피터 팬","자유로운 상상력의 세계를 보여줍니다."),
("톰 소여의 모험","모험과 성장의 즐거움을 느낄 수 있습니다."),
("이상한 나라의 앨리스","창의적 사고를 자극하는 이야기입니다.")
],
"lesson":"세상을 다양한 시각으로 바라보는 힘을 기를 수 있습니다.",
"question":"어른이 되어도 잃지 말아야 할 것은 무엇일까요?",
"quote":"호기심은 새로운 세상의 문을 연다."
},

"ISTJ":{
"desc":"책임감 있고 현실적인 계획가형입니다.",
"books":[
("로빈슨 크루소","문제를 해결하는 지혜를 보여줍니다."),
("80일간의 세계일주","목표를 향한 끈기를 배울 수 있습니다."),
("플랜더스의 개","성실함과 인간성을 생각하게 합니다.")
],
"lesson":"꾸준함과 책임감이 얼마나 중요한지 배울 수 있습니다.",
"question":"어려움 속에서도 포기하지 않게 만드는 힘은 무엇일까요?",
"quote":"성실함은 가장 강력한 능력이다."
}

}

st.divider()

if st.button("📚 책 추천 받기"):
    
    if mbti in data:
        info = data[mbti]

        st.balloons()

        st.subheader(f"✨ {mbti} 유형")

        st.info(info["desc"])

        st.subheader("📖 추천 도서")

        for book in info["books"]:
            st.write(f"**{book[0]}**")
            st.write(f"👉 {book[1]}")
            st.write("")

        st.subheader("💡 이 책이 주는 영감")
        st.success(info["lesson"])

        st.subheader("❓ 생각해볼 질문")
        st.warning(info["question"])

        st.subheader("🌟 오늘의 명언")
        st.write(f"\"{info['quote']}\"")

    else:
        st.write("이 MBTI 유형의 데이터는 아직 준비 중입니다 🙂")
