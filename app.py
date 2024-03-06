import streamlit as st
from pyzbar import pyzbar
import numpy as np
from PIL import Image 
import pandas as pd

def main():

    SHEET_ID = '1Ps6OqL1cLdCiD30VJTkDhSWKNYW2I7Uqhg1viCBvFXQ'
    SHEET_NAME = 'test'
    foglio_id=0
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}/edit#gid={foglio_id}'
    df = pd.read_csv(url,dtype={'Collo':str})

    def barcode(image):
        # decodes all barcodes from an image
        decoded_objects = pyzbar.decode(image)
        barcode = []
        for obj in decoded_objects:
            barcode.append(obj.data)
        return barcode

    st.title("Barcode Fren'z App")
    file_image = st.camera_input(label = "Camera Frontale")

    if file_image:
        input_img = Image.open(file_image)
        #flipped_img = input_img.transpose(Image.FLIP_LEFT_RIGHT)
        one, two = st.columns(2)
        with one:
            pass
            # st.write("**Barcode**")
            # st.image(flipped_img, use_column_width=True)
        with two:
            pass
        if st.button("Verifica Barcode"):
            #################################################
            #flipped_img = Image.open("test.jpg")
            image = np.array(input_img) # convert to array
            st.image(image, caption='Uploaded Image', use_column_width=True)
            barcodes = barcode(image)
            if barcodes:
                st.success("Barcodes TROVATO:")
                for barcode in barcodes:
                    bar = barcode.decode('utf-8')
                    st.write(bar)
                    st.dataframe(df[df['Collo']==bar])
            else:
                st.error("NON CI SONO BARCODE NELLA FOTO!!!!!!")
            #################################################
    else:
        st.write("Scatta la foto per Classificare il Barcode")

if __name__ == '__main__':
    main()

