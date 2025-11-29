from pil_conversion import *
from PIL import Image
import streamlit as st

st.title("Jackfruit Problem : Image Processing")

uploaded_img = st.file_uploader('Upload Image', type = ["jpg", "jpeg", "png"])
if uploaded_img is not None:
    st.image(uploaded_img)
    img = Image.open(uploaded_img)
    img_mode = get_image_mode(img)

    if img_mode in  ["RGB","RGBA"] :
        img = img.convert('RGB')
        gray_img = convert2gray(img)
        st.image(gray_img, caption='Converted Image')

        dom_secondary_colors = dom_secondarycolor(img)

        table_data = [
            {"Metric": "Red Pixel Count", "Value": red_pixel_count(img)},
            {"Metric": "Dominant Primary Color", "Value": dom_primarycolor(img)},
            {"Metric": "Dominant Secondary Color", "Value": str(dom_secondary_colors)},
        ]

        st.table(table_data)

    else:
        st.warning('Please upload an image in RGB/RGBA', icon="⚠️")    
