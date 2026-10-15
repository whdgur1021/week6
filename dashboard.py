import streamlit as st
import pandas as pd

# 앱 제목과 안내
st.title('공부 습관 대시보드')
st.write('공부시간과 점수의 관계를 살펴봅니다.')

# 1. 데이터 불러오기
df = pd.read_csv('study.csv')

# 2. 요약 지표 3개를 한 줄에
col1, col2, col3 = st.columns(3)
col1.metric('학생 수(명)', len(df))
col2.metric('평균 점수(점)', round(df['점수'].mean(), 1))
col3.metric('평균 공부시간(시간)', round(df['공부시간'].mean(), 1))

# 3. 원본 표는 펼쳐 보기로
with st.expander('원본 데이터 보기'):
    st.dataframe(df)

# 4. 슬라이더로 조건 고르기
min_hour = st.slider('최소 공부시간', 0.0, 5.0, 0.0, 0.5)
filtered = df[df['공부시간'] >= min_hour]
st.write(f'선택된 학생: {len(filtered)}명')

# 5. 차트 2개
st.subheader('공부시간과 점수')
st.scatter_chart(filtered, x='공부시간', y='점수')

st.subheader('학생별 점수')
st.bar_chart(filtered, x='학생ID', y='점수')