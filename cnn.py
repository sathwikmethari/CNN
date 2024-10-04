# Importing the libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import keras
import numpy as np
from tensorflow.keras.preprocessing import image

#tf.__version__

cnn = keras.models.load_model("models/cnn.keras")

import streamlit as st
st.title("CNN-APP")


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    test_image = image.load_img(uploaded_file, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image)

    if result[0][0] == 1:
        st.write('DOG')
    else:
        st.write('CAT')

    