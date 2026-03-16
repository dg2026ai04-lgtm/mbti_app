import streamlit as st
st.title('나만의 MBTI 앱!')
st.write('여기에 무엇을 넣어볼까요?!')
import streamlit as st

st.set_page_config(
    page_title="MBTI 영화 추천",
    page_icon="🎬"
)

st.title("🎬 MBTI 기반 영화 & 포켓몬 추천")
st.write("당신의 MBTI 성격에 맞는 **영화와 포켓몬**을 추천합니다! ✨")

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
"pokemon_reason":"높은 지능과 전략적 사고를 가진 포켓몬으로 INTJ와 잘 어울립니다.",
"movie":"",
"movie_reason":"복잡한 구조와 깊은 사고가 필요한 이야기라 전략적 사고를 좋아하는 INTJ에게 잘 맞습니다.",
"quote":"오늘의 작은 계획이 미래의 큰 성공을 만든다."
},

"INTP":{
"pokemon":"알카자람",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
"pokemon_reason":"지능이 높은 초능력 포켓몬으로 탐구형 INTP와 닮았습니다.",
"movie":"",
"movie_reason":"현실과 철학적 질문을 던지는 영화라 논리적 사고를 좋아하는 INTP에게 흥미롭습니다.",
"quote":"질문하는 순간 새로운 세계가 열린다."
},

"ENTJ":{
"pokemon":"리자몽",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pokemon_reason":"강력한 리더십을 가진 포켓몬입니다.",
"movie":"",
"movie_reason":"강한 리더십과 목표를 향한 의지가 돋보이는 이야기입니다.",
"quote":"도전은 리더를 성장시킨다."
},

"ENTP":{
"pokemon":"로토무",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/479.png",
"pokemon_reason":"창의적이고 장난기 많은 성격입니다.",
"movie":"",
"movie_reason":"창의적인 아이디어와 시간여행 설정이 ENTP의 상상력을 자극합니다.",
"quote":"새로운 아이디어는 세상을 바꿀 수 있다."
},

"INFJ":{
"pokemon":"가디안",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png",
"pokemon_reason":"타인을 보호하는 따뜻한 포켓몬입니다.",
"movie":"",
"movie_reason":"삶의 의미와 진정한 자유에 대해 깊이 생각하게 합니다.",
"quote":"당신의 진심은 누군가에게 큰 힘이 된다."
},

"INFP":{
"pokemon":"이브이",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
"pokemon_reason":"가능성이 많은 포켓몬입니다.",
"movie":"",
"movie_reason":"상상력과 감성이 풍부한 이야기라 INFP에게 영감을 줍니다.",
"quote":"자신의 꿈을 믿는 것이 가장 큰 용기다."
},

"ENFJ":{
"pokemon":"루카리오",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
"pokemon_reason":"정의감이 강한 포켓몬입니다.",
"movie":"",
"movie_reason":"다른 사람에게 영감을 주는 이야기입니다.",
"quote":"당신의 격려 한마디가 세상을 바꿀 수 있다."
},

"ENFP":{
"pokemon":"피카츄",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pokemon_reason":"밝고 긍정적인 에너지를 가진 포켓몬입니다.",
"movie":"",
"movie_reason":"모험과 자기 발견의 이야기라 ENFP에게 잘 맞습니다.",
"quote":"오늘의 즐거움이 내일의 에너지가 된다."
},

"ISTJ":{
"pokemon":"거북왕",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
"pokemon_reason":"책임감 있는 포켓몬입니다.",
"movie":"",
"movie_reason":"책임감과 문제 해결 능력이 중요한 이야기입니다.",
"quote":"꾸준함은 가장 강한 힘이다."
},

"ISFJ":{
"pokemon":"해피너스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
"pokemon_reason":"다른 포켓몬을 돌보는 따뜻한 포켓몬입니다.",
"movie":"",
"movie_reason":"따뜻한 마음과 가족의 의미를 보여주는 영화입니다.",
"quote":"작은 친절이 큰 변화를 만든다."
},

"ESTJ":{
"pokemon":"마기라스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
"pokemon_reason":"강력한 지도자 같은 포켓몬입니다.",
"movie":"",
"movie_reason":"팀워크와 책임감을 보여주는 이야기입니다.",
"quote":"책임감은 신뢰를 만든다."
},

"ESFJ":{
"pokemon":"픽시",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
"pokemon_reason":"사람을 돕는 따뜻한 포켓몬입니다.",
"movie":"",
"movie_reason":"사람과 사랑, 가족의 의미를 느낄 수 있습니다.",
"quote":"사람을 향한 마음이 세상을 밝힌다."
},

"ISTP":{
"pokemon":"스라크",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png",
"pokemon_reason":"행동력 있는 포켓몬입니다.",
"movie":"",
"movie_reason":"빠른 판단과 행동 중심의 이야기입니다.",
"quote":"직접 해보는 것이 최고의 배움이다."
},

"ISFP":{
"pokemon":"라프라스",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
"pokemon_reason":"감성적인 포켓몬입니다.",
"movie":"",
"movie_reason":"아름다운 영상과 감성적인 이야기가 ISFP에게 잘 맞습니다.",
"quote":"자신의 마음을 믿어도 괜찮다."
},

"ESTP":{
"pokemon":"초염몽",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
"pokemon_reason":"에너지 넘치는 포켓몬입니다.",
"movie":"",
"movie_reason":"스릴과 모험을 좋아하는 ESTP에게 잘 맞습니다.",
"quote":"도전하는 순간 성장이 시작된다."
},

"ESFP":{
"pokemon":"푸린",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
"pokemon_reason":"사람들을 즐겁게 하는 포켓몬입니다.",
"movie":"",
"movie_reason":"즐거움과 에너지가 가득한 이야기입니다.",
"quote":"웃음은 가장 강한 에너지다."
}

}

st.divider()

if st.button("🎬 추천 보기"):

    info = data[mbti]

    st.balloons()

    st.subheader(f"✨ {mbti} 유형")

    st.subheader("⚡ 추천 포켓몬")
    st.image(info["img"], width=200)
    st.write(info["pokemon"])
    st.write("👉", info["pokemon_reason"])

    st.subheader("🎬 추천 영화")
    st.write(info["movie"])
    st.write("👉", info["movie_reason"])

    st.subheader("🌟 오늘의 명언")
    st.success(info["quote"])
    
