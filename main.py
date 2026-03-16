import streamlit as st
st.title('나만의 MBTI 앱!')
st.write('여기에 무엇을 넣어볼까요?!')

import streamlit as st

st.set_page_config(
    page_title="MBTI 영화 추천",
    page_icon="🎬"
)

st.title("🎬 MBTI 기반 영화 & 포켓몬 추천")
st.write("MBTI 성격에 맞는 **포켓몬과 영화**를 추천합니다! ✨")

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
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"pokemon_reason":"전략적이고 지능적인 성격이 INTJ와 닮았습니다.",
"movie":"Inception",
"poster":"https://m.media-amazon.com/images/I/51zUbui+gbL.jpg",
"movie_reason":"복잡한 구조와 깊은 사고가 필요한 이야기라 INTJ에게 잘 맞습니다.",
"quote":"오늘의 작은 계획이 미래의 큰 성공을 만든다."
},

"INTP":{
"pokemon":"알카자람",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
"pokemon_reason":"높은 지능을 가진 포켓몬입니다.",
"movie":"The Matrix",
"poster":"https://m.media-amazon.com/images/I/51EG732BV3L.jpg",
"movie_reason":"현실과 철학적 질문을 던지는 영화입니다.",
"quote":"질문하는 순간 새로운 세계가 열린다."
},

"ENTJ":{
"pokemon":"리자몽",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pokemon_reason":"강력한 리더십을 가진 포켓몬입니다.",
"movie":"Gladiator",
"poster":"https://m.media-amazon.com/images/I/51A9ZJ3ZK1L.jpg",
"movie_reason":"리더십과 목표 의지가 강조되는 이야기입니다.",
"quote":"도전은 리더를 성장시킨다."
},

"ENTP":{
"pokemon":"로토무",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/479.png",
"pokemon_reason":"창의적이고 장난기 있는 성격입니다.",
"movie":"Back to the Future",
"poster":"https://m.media-amazon.com/images/I/51G8N0RZP7L.jpg",
"movie_reason":"기발한 아이디어와 시간여행 설정이 ENTP와 잘 맞습니다.",
"quote":"새로운 아이디어는 세상을 바꿀 수 있다."
},

"INFJ":{
"pokemon":"가디안",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png",
"pokemon_reason":"다른 사람을 보호하는 포켓몬입니다.",
"movie":"The Truman Show",
"poster":"https://m.media-amazon.com/images/I/51U9oF9q9-L.jpg",
"movie_reason":"삶의 의미와 진정한 자유를 생각하게 합니다.",
"quote":"당신의 진심은 누군가에게 큰 힘이 된다."
},

"INFP":{
"pokemon":"이브이",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
"pokemon_reason":"다양한 가능성을 가진 포켓몬입니다.",
"movie":"Spirited Away",
"poster":"https://m.media-amazon.com/images/I/51hJc0Lk5LL.jpg",
"movie_reason":"상상력과 감성이 풍부한 이야기입니다.",
"quote":"자신의 꿈을 믿는 것이 가장 큰 용기다."
},

"ENFJ":{
"pokemon":"루카리오",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
"pokemon_reason":"정의감과 리더십을 가진 포켓몬입니다.",
"movie":"Dead Poets Society",
"poster":"https://m.media-amazon.com/images/I/51qmhXWZBxL.jpg",
"movie_reason":"사람들에게 영감을 주는 이야기입니다.",
"quote":"당신의 격려 한마디가 세상을 바꿀 수 있다."
},

"ENFP":{
"pokemon":"피카츄",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pokemon_reason":"밝고 긍정적인 에너지의 포켓몬입니다.",
"movie":"The Secret Life of Walter Mitty",
"poster":"https://m.media-amazon.com/images/I/51yB9dC5TLL.jpg",
"movie_reason":"모험과 자기 발견의 이야기입니다.",
"quote":"오늘의 즐거움이 내일의 에너지가 된다."
},

"ISTJ":{
"pokemon":"거북왕",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
"pokemon_reason":"책임감 있는 포켓몬입니다.",
"movie":"Apollo 13",
"poster":"https://m.media-amazon.com/images/I/51Z6S0U9PCL.jpg",
"movie_reason":"책임감과 문제 해결 능력을 보여줍니다.",
"quote":"꾸준함은 가장 강한 힘이다."
},

"ISFJ":{
"pokemon":"해피너스",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
"pokemon_reason":"다른 포켓몬을 돌보는 따뜻한 포켓몬입니다.",
"movie":"Paddington",
"poster":"https://m.media-amazon.com/images/I/51N6cK9k5PL.jpg",
"movie_reason":"따뜻한 가족 이야기입니다.",
"quote":"작은 친절이 큰 변화를 만든다."
},

"ESTJ":{
"pokemon":"마기라스",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
"pokemon_reason":"강한 지도자 같은 포켓몬입니다.",
"movie":"Top Gun",
"poster":"https://m.media-amazon.com/images/I/51iQG6JvX2L.jpg",
"movie_reason":"팀워크와 책임감을 보여줍니다.",
"quote":"책임감은 신뢰를 만든다."
},

"ESFJ":{
"pokemon":"픽시",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
"pokemon_reason":"사람을 돕는 따뜻한 포켓몬입니다.",
"movie":"The Sound of Music",
"poster":"https://m.media-amazon.com/images/I/51d4y3m6NML.jpg",
"movie_reason":"사람과 사랑, 가족의 의미를 보여줍니다.",
"quote":"사람을 향한 마음이 세상을 밝힌다."
},

"ISTP":{
"pokemon":"스라크",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png",
"pokemon_reason":"행동력이 뛰어난 포켓몬입니다.",
"movie":"Mad Max: Fury Road",
"poster":"https://m.media-amazon.com/images/I/51nZpYqK1OL.jpg",
"movie_reason":"빠른 판단과 행동 중심 이야기입니다.",
"quote":"직접 해보는 것이 최고의 배움이다."
},

"ISFP":{
"pokemon":"라프라스",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
"pokemon_reason":"감성적인 포켓몬입니다.",
"movie":"Life of Pi",
"poster":"https://m.media-amazon.com/images/I/51k0qa6pVHL.jpg",
"movie_reason":"아름다운 영상과 감성적인 이야기입니다.",
"quote":"자신의 마음을 믿어도 괜찮다."
},

"ESTP":{
"pokemon":"초염몽",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
"pokemon_reason":"에너지 넘치는 포켓몬입니다.",
"movie":"Jurassic Park",
"poster":"https://m.media-amazon.com/images/I/51H0N0p6GQL.jpg",
"movie_reason":"스릴 넘치는 모험 이야기입니다.",
"quote":"도전하는 순간 성장이 시작된다."
},

"ESFP":{
"pokemon":"푸린",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
"pokemon_reason":"사람들을 즐겁게 하는 포켓몬입니다.",
"movie":"The Greatest Showman",
"poster":"https://m.media-amazon.com/images/I/51b5YG6Y1rL.jpg",
"movie_reason":"즐거움과 에너지가 가득한 영화입니다.",
"quote":"웃음은 가장 강한 에너지다."
}

}

st.divider()

if st.button("🎬 추천 보기"):

    info = data[mbti]

    st.balloons()

    st.subheader(f"✨ {mbti} 유형")

    st.subheader("⚡ 추천 포켓몬")
    st.image(info["pokemon_img"], width=150)
    st.write(info["pokemon"])
    st.write("👉", info["pokemon_reason"])

    st.subheader("🎬 추천 영화")
    st.image(info["poster"], width=250)
    st.write("영화 제목:", info["movie"])
    st.write("👉", info["movie_reason"])

    st.subheader("🌟 오늘의 명언")
    st.success(info["quote"])
