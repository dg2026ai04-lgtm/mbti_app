import streamlit as st
st.title('나만의 MBTI 앱!')
st.write('여기에 무엇을 넣어볼까요?!')
import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="MBTI 독서 & 포켓몬 추천",
    page_icon="📚"
)

st.title("📚 MBTI 기반 독서 & 포켓몬 추천 앱")
st.write("성격 유형에 맞는 **책, 포켓몬, 그리고 오늘의 명언**을 통해 새로운 영감을 얻어보세요 ✨")

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

"INTJ":{
"pokemon":"뮤츠",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"pokemon_reason":"깊은 사고와 전략적 지능을 가진 포켓몬으로 INTJ와 닮았습니다.",
"books":["어린 왕자","1984","멋진 신세계"],
"desc":"전략적이고 미래지향적인 사고를 하는 사색가형입니다.",
"lesson":"세상을 분석하고 더 나은 미래를 설계하는 통찰력을 기를 수 있습니다.",
"quote":"오늘의 작은 계획이 미래의 큰 성공을 만든다."
},

"INTP":{
"pokemon":"알카자람",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
"pokemon_reason":"높은 지능과 초능력을 가진 포켓몬으로 탐구형 INTP와 잘 어울립니다.",
"books":["이상한 나라의 앨리스","프랑켄슈타인","걸리버 여행기"],
"desc":"논리적이고 호기심이 많은 탐구형 사상가입니다.",
"lesson":"비판적 사고와 창의적인 질문 능력을 키울 수 있습니다.",
"quote":"질문하는 순간 새로운 세계가 열린다."
},

"ENTJ":{
"pokemon":"리자몽",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pokemon_reason":"강한 리더십과 카리스마를 가진 포켓몬입니다.",
"books":["해리 포터","삼총사","몬테크리스토 백작"],
"desc":"목표지향적이고 리더십이 강한 지도자형입니다.",
"lesson":"목표를 이루기 위한 전략과 책임감을 배울 수 있습니다.",
"quote":"도전은 리더를 성장시킨다."
},

"ENTP":{
"pokemon":"로토무",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/479.png",
"pokemon_reason":"창의적이고 장난기 있는 성격이 ENTP와 닮았습니다.",
"books":["80일간의 세계일주","이상한 나라의 앨리스","걸리버 여행기"],
"desc":"창의적이고 아이디어가 풍부한 발명가형입니다.",
"lesson":"새로운 생각으로 문제를 해결하는 능력을 키울 수 있습니다.",
"quote":"새로운 아이디어는 세상을 바꿀 수 있다."
},

"INFJ":{
"pokemon":"가디안",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png",
"pokemon_reason":"다른 사람을 보호하는 따뜻한 포켓몬입니다.",
"books":["모모","어린 왕자","데미안"],
"desc":"통찰력이 깊고 이상을 추구하는 조언가형입니다.",
"lesson":"자기 이해와 인간 관계의 깊이를 배울 수 있습니다.",
"quote":"당신의 진심은 누군가에게 큰 힘이 된다."
},

"INFP":{
"pokemon":"이브이",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
"pokemon_reason":"다양한 가능성을 가진 포켓몬입니다.",
"books":["빨강머리 앤","나니아 연대기","어린 왕자"],
"desc":"감수성이 풍부한 이상주의자입니다.",
"lesson":"자신의 가치와 꿈을 지키는 용기를 배울 수 있습니다.",
"quote":"자신의 꿈을 믿는 것이 가장 큰 용기다."
},

"ENFJ":{
"pokemon":"루카리오",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
"pokemon_reason":"정의감과 리더십을 가진 포켓몬입니다.",
"books":["작은 아씨들","비밀의 화원","플랜더스의 개"],
"desc":"사람을 이끄는 따뜻한 지도자형입니다.",
"lesson":"공감과 협력의 가치를 배울 수 있습니다.",
"quote":"당신의 격려 한마디가 세상을 바꿀 수 있다."
},

"ENFP":{
"pokemon":"피카츄",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pokemon_reason":"밝고 긍정적인 에너지를 가진 포켓몬입니다.",
"books":["피터 팬","톰 소여의 모험","이상한 나라의 앨리스"],
"desc":"열정적이고 상상력이 풍부한 활동가형입니다.",
"lesson":"세상을 다양한 시각으로 바라보는 힘을 기를 수 있습니다.",
"quote":"오늘의 즐거움이 내일의 에너지가 된다."
},

"ISTJ":{
"pokemon":"거북왕",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
"pokemon_reason":"안정감과 책임감을 가진 포켓몬입니다.",
"books":["로빈슨 크루소","80일간의 세계일주","플랜더스의 개"],
"desc":"책임감 있고 현실적인 계획가형입니다.",
"lesson":"꾸준함과 책임감의 중요성을 배울 수 있습니다.",
"quote":"꾸준함은 가장 강한 힘이다."
},

"ISFJ":{
"pokemon":"해피너스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
"pokemon_reason":"다른 포켓몬을 돌보는 따뜻한 포켓몬입니다.",
"books":["플랜더스의 개","작은 아씨들","비밀의 화원"],
"desc":"따뜻하고 책임감 있는 보호자형입니다.",
"lesson":"배려와 공감의 가치를 배울 수 있습니다.",
"quote":"작은 친절이 큰 변화를 만든다."
},

"ESTJ":{
"pokemon":"마기라스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
"pokemon_reason":"강력하고 조직적인 힘을 가진 포켓몬입니다.",
"books":["삼총사","해리 포터","80일간의 세계일주"],
"desc":"체계적이고 조직적인 지도자형입니다.",
"lesson":"협력과 리더십의 중요성을 배울 수 있습니다.",
"quote":"책임감은 신뢰를 만든다."
},

"ESFJ":{
"pokemon":"픽시",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
"pokemon_reason":"따뜻하고 사람을 돕는 포켓몬입니다.",
"books":["작은 아씨들","비밀의 화원","플랜더스의 개"],
"desc":"친절하고 사교적인 협력가형입니다.",
"lesson":"공감과 관계의 중요성을 배울 수 있습니다.",
"quote":"사람을 향한 마음이 세상을 밝힌다."
},

"ISTP":{
"pokemon":"스라크",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png",
"pokemon_reason":"행동력과 문제 해결 능력이 뛰어난 포켓몬입니다.",
"books":["로빈슨 크루소","보물섬","80일간의 세계일주"],
"desc":"논리적이고 실용적인 문제 해결가입니다.",
"lesson":"도전과 경험을 통해 배우는 능력을 기를 수 있습니다.",
"quote":"직접 해보는 것이 최고의 배움이다."
},

"ISFP":{
"pokemon":"라프라스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
"pokemon_reason":"온화하고 감성적인 포켓몬입니다.",
"books":["어린 왕자","비밀의 화원","빨강머리 앤"],
"desc":"감성적이고 예술적인 자유로운 영혼입니다.",
"lesson":"자신만의 감성과 아름다움을 발견할 수 있습니다.",
"quote":"자신의 마음을 믿어도 괜찮다."
},

"ESTP":{
"pokemon":"초염몽",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
"pokemon_reason":"불꽃처럼 에너지 넘치는 포켓몬입니다.",
"books":["보물섬","톰 소여의 모험","80일간의 세계일주"],
"desc":"활동적이고 도전을 좋아하는 모험가입니다.",
"lesson":"새로운 도전을 통해 성장하는 법을 배울 수 있습니다.",
"quote":"도전하는 순간 성장이 시작된다."
},

"ESFP":{
"pokemon":"푸린",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
"pokemon_reason":"사람들을 즐겁게 하는 포켓몬입니다.",
"books":["피터 팬","톰 소여의 모험","빨강머리 앤"],
"desc":"즐거움과 에너지를 나누는 자유로운 연예인형입니다.",
"lesson":"긍정적인 태도의 중요성을 배울 수 있습니다.",
"quote":"웃음은 가장 강한 에너지다."
}

}

st.divider()

if st.button("📚 추천 보기"):

    info = data[mbti]

    st.balloons()

    st.subheader(f"✨ {mbti} 유형")

    st.info(info["desc"])

    st.subheader("⚡ 추천 포켓몬")
    st.image(info["img"], width=200)
    st.write(info["pokemon"])
    st.write("👉", info["pokemon_reason"])

    st.subheader("📚 추천 도서")
    for book in info["books"]:
        st.write("📖", book)

    st.subheader("💡 독서를 통해 얻는 영감")
    st.success(info["lesson"])

    st.subheader("🌟 오늘의 명언")
    st.write(f"\"{info['quote']}\"")
