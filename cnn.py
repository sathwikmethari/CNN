# Importing the libraries
import tensorflow as tf
import keras
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing import image

st.set_page_config(
    layout="wide"    
)

#tf.__version__
@st.cache_data
def load_model():
    cnn = keras.models.load_model("models/cnn.keras")
    return cnn  

cnn=load_model()
st.title("CNN-APP")
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    try:
        test_image = image.load_img(uploaded_file, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = cnn.predict(test_image)

        with col2:
            st.image(uploaded_file)

        with st.container():
            st.header("RESULT", divider="gray")
            if result[0][0] == 1:
                st.write('YOU UPLOADED A PICTURE OF A :blue-background[DOG]')
            else:
                st.write('YOU UPLOADED A PICTURE OF A :blue-background[CAT]')

    except:
        st.write("Upload either JPG or JPEG type file!")

    