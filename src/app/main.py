import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import model_from_json
import tensorflow as tf
from PIL import Image, ImageDraw, ImageFont
from keras.preprocessing import image

# Obtém o caminho absoluto para o arquivo JSON
file_path_json = 'src/models/model_093/classificador_093.json'
file_path_weigths = 'src/models/model_093/weigths_classificador_0.93.h5'

def load_model(path1, path2):
    with open(path1, 'r') as f:
        model = f.read()
    model = model_from_json(model)
    model.load_weights(path2)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Configuração do app Streamlit
st.title('Diagnóstico de Retinopatia Diabética')
st.write('Faça o upload de uma imagem para prever o diagnóstico')

# # Upload da imagem
img_input = st.file_uploader("Escolha uma imagem", type=['jpg', 'jpeg'], accept_multiple_files=False)

if img_input is not None:

    img = Image.open(img_input)
    st.write("Imagem Enviada:")
    st.image(img, caption='Imagem carregada', use_column_width=False, width=500)

    # Pré-processamento da imagem para fazer a previsão
    img = img.resize((224, 224))  # Redimensionar a imagem para o tamanho esperado pelo modelo
    img_cp = img.copy()
    img = image.img_to_array(img)
    img = img / 255
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))

    # st.image(img, caption='Imagem enviada', use_column_width=False, width=200)

    # Realizar a previsão
    # st.write("Fazendo previsão...")
    model = load_model(file_path_json, file_path_weigths)
    prediction_pct = model.predict(img)
    prediction = np.argmax(prediction_pct, axis=1)[0]

    # Exibir a imagem editada com o diagnóstico sobreposto
    st.write("Imagem com Diagnóstico:")


    # Colocar um texto na imagem
    draw = ImageDraw.Draw(img_cp)
    # Escolher a fonte e o tamanho
    font = ImageFont.load_default()  # Substitua pela fonte desejada e pelo tamanho
    # Texto a ser escrito
    text = "DR: Positive"
    # Tamanho do texto
    text_width, text_height = draw.textsize(text, font=font)
    # Coordenadas para o canto inferior direito
    image_width, image_height = img_cp.size
    margin = 1
    text_position = (image_width - text_width - margin, image_height - text_height - margin)
    # Escrever o texto na imagem


    # Lógica para interpretar a previsão e exibir o diagnóstico
    if prediction == 0:
        draw.text(text_position, 'DR: Positive', fill="white", font=font)
        st.image(img_cp, caption='Diagnóstico sobreposto', use_column_width=False, width=500)
        st.write("Diagnóstico:")
        st.markdown(f'Paciente com<span style="color: red;"> Retinopatia Diabética</span> com {(prediction_pct[0][prediction]):.2%}.', unsafe_allow_html=True)
    else:
        draw.text(text_position, 'DR: Negative', fill="white", font=font)
        st.image(img_cp, caption='Diagnóstico sobreposto', use_column_width=False, width=500)
        st.write("Diagnóstico:")
        st.markdown(f'Paciente<span style="color: blue;"> Normal</span> com {(prediction_pct[0][prediction]):.2%}.', unsafe_allow_html=True)

