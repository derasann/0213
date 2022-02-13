import streamlit as st
from PIL import Image

st.title('Happy valentine')

st.write('Display Image')

if st.checkbox('x2+(y−3x2‾‾√)2=1'):
    img = Image.open('./cardioid.jpg')
    st.image(img, caption='だいすき', use_column_width=True)

if st.checkbox('こんど一緒にいく'):
    img = Image.open('./Maker.jpg')
    st.image(img, caption='東京は9月3,4日', use_column_width=True)


