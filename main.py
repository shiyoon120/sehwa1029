import streamlit as st
st.title('김시윤의 첫번째 앱!')
st.subheader('안녕안녕')
st.write('배불러..')
st.write('https://naver.com')
st.link_button('네이버 바로가기','https://naver.com')

name = st.text_input('이름을 입력해주세요!:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!')
    st.balloons()
    st.image('https://file2.nocutnews.co.kr/newsroom/image/2024/10/19/202410191639106350_0.jpg')
    st.video('https://youtu.be/BsDPox8ZvQw?si=EZmGxchCIlN-dbtN')

st.success('성공!')
st.warning('경고!')
st.error('오류!')
st.info('안내문')
