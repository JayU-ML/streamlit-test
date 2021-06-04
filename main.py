import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('streamlitあぷり！')
st.write('プログレスバー！')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

# st.write('Display Image')

left_col, right_col = st.beta_columns(2)
button = left_col.button('右カラムに文字を表示！')
if button:
    right_col.write('右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')

if st.checkbox('Show Image'):
    img = Image.open('image.png')
    st.image(img, caption="Jun-Jun", use_column_width=True)

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

# df = pd.read_csv(
#     '/Users/jumpeismacbookpro2.0/Documents/dev/streamlit/map_float.csv')

# df.iloc[:, 0]

# st.map(df)
# st.line_chart(df)
# st.area_chart(df)
# st.table(df)
