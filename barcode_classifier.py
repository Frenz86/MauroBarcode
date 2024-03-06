import streamlit as st
import cv2
from pyzbar import pyzbar
import numpy as np

def main():

    import pandas as pd
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


    st.title('Barcode Decoder App')
    # uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"]) 
    # if uploaded_image is not None:
    #     file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    ###########################################################
    from PIL import Image
    #image = cv2.imread("test.jpg")
    image = Image.open("test.jpg")
    image = np.array(image) # convert to array
    st.image(image, caption='Uploaded Image', use_column_width=True)
    barcodes = barcode(image)
    if barcodes:
        st.write("Barcodes detected:")
        for barcode in barcodes:
            bar = barcode.decode('utf-8')
            st.write(bar)
            st.dataframe(df[df['Collo']==bar])
    else:
        st.write("No barcodes detected in the image.")
    
if __name__ == '__main__':
    main()

