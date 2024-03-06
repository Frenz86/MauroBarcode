import streamlit as st 
import numpy as np 
from PIL import Image 

file_image = st.camera_input(label = "Camera Frontale")

if file_image:
    input_img = Image.open(file_image)
    flipped_img = input_img.transpose(Image.FLIP_LEFT_RIGHT)
    one, two = st.columns(2)
    with one:
        st.write("**Barcode**")
        st.image(flipped_img, use_column_width=True)
    with two:
        pass
    if st.button("Verifica Barcode"):
        st.write('Download completed')
   
else:
    st.write("Scatta la foto per Classificare il Barcode")