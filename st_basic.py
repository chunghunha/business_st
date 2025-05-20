import streamlit as st

'# 🚗: 일반 텍스트'
st.write('# 마크다운 H1 : st.write()')
st.write('## 마크다운 H2 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('#### 마크다운 H4 : st.write()')
st.write('##### 마크다운 H5 : st.write()')
st.write('###### 마크다운 H6 : st.write()')
st.write('') # 빈 줄 추가

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')

st.write('')

st.markdown('## 마크다운 : st.markdown()')
st.markdown(
    '''
    # 마크다운 헤더1
    - __마크다운__ 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록2-1
        - 마크다운 목록2-2
            - 마크다운 목록3-1
                - 마크다운 목록4-1

    # 마크다운 헤더1-2
    1. __마크다운__ 목록1. **굵게** 표시
    1. 마크다운 목록2. *기울임* 표시  
        1. 마크다운 목록2-1   
        1. 마크다운 목록2-2
            - 마크다운 목록3-1
                - 마크다운 목록4-1

    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)
    - [하정훈 스트림릿](https://buisinesshoingik.streamlit.app/)

    ### 마크다운 헤더3
    일반 텍스트
    '''
)



st.divider()  # 👈 구분선

'# 🚗: 형식이 있는 텍스트'
st.caption('작은글씨, ')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

st.write('##### 코드 블록: st.code()')

st.code('print("Hello, World!")', language='python')

st.code('''
print("Hello, World!")
a=10
b=30
st.write(a+b)
''', 
language='cpp',
line_numbers=True
)

st.code('print("Hello, World!")', language='python', line_numbers=True)

st.write('##### 코드 블록: Markdown')
st.write(
    '''
    이것은 코드블록입니다.
    ```python
    print("Hello, World!")
    ```
    '''
)

st.write('##### 코드+결과: st.echo()')
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    age = 30
    height = 175
    st.write(f"Hello, Streamlit! {name}, {age}, {height}")


st.write('##### Latex 수식 작성: st.latex()')

st.latex('\int_a^b f(x)dx')
st.latex('\sum_{x=1}^{n} \simeq \\frac{f(x)}{dx}')

st.write('##### Latex 수식 작성: Markdown')
st.write('이것은 Latex를 사용한 문장입니다. $\int_a^b \\frac{f(x)}{dx}$ 이렇게 중간에 표시할 수 있습니다.')

'''### 👑 Magic 적용
1. ordered item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

'''#### 텍스트 색상 변경
:red[**색상**]이 있는 :green[*텍스트*]를 :orange[***작성***]할 수 있습니다.
- :red[빨간색 텍스트]
- :blue[파란색 텍스트]
- :green[초록색 텍스트]
- :orange[주황색 텍스트]
- :gray[회색 텍스트]
'''

'# 📚: 콜아웃'

'#### :orange[정보: st.info()]'
st.info(
    icon="ℹ️",
    body='''
    **:sunglasses: 이것은 정보를 제공하는 콜아웃입니다.** 
    - :red[빨간색 텍스트]
        - :blue[파란색 텍스트]
    - :green[초록색 텍스트]
        - :orange[주황색 텍스트]
    '''
)

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon="🚫")

'#### :orange[성공: st.success()]'
st.success('This is a success message', icon="✅")

'# 🎥: 이미지, 오디오, 동영상'

'#### :orange[이미지: st.image()]'
st.image("bpbp.jpg", caption="하정훈 교수1", width=200)

'#### :orange[오디오: st.audio()]'
st.audio("edm.mp3", format="audio/mpeg", loop=True)

'#### :orange[동영상: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open("sample-5s.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()  # 👈 구분선

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=["a", "b", "c"]
    )

chart_data

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"],
)
st.map(df)

st.divider()  # 👈 구분선

'# :blue[시각화 라이브러리]'

'#### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 👈 차트 출력

st.divider()  # 👈 구분선

'#### :orange[Altair: st.altair_chart()]'
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=["a", "b", "c"]
    )

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(
       x="a", y="b", 
       size="c", 
       color="c", 
       tooltip=["a", "b", "c"]
       )
)

st.altair_chart(c, use_container_width=True)

'#### :orange[Plotly: st.plotly_chart()]'
import plotly.express as px

df = px.data.iris()  
fig = px.scatter(df, x="sepal_width", y="sepal_length")

st.plotly_chart(fig, key="iris", on_select="rerun")
