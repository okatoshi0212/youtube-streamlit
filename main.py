from tkinter.tix import TEXT
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトル
st.title('野菜判別アプリ')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容3の回答')



#サイドバー（左側に表示）
#text = st.text_input('あなたの選んだ野菜の種類を教えてください')
#agi = st.slider('あなたの好きな味は？', 0, 100, 50)

#'あなたの選んだもの：', text
#'味：', agi


#チェックボックス（画像表示有無）
#if st.checkbox('Swho Image'):
 #   img = Image.open('78022896.jpg')
  #  st.image(img, caption='ピーマン', use_column_width=True)
