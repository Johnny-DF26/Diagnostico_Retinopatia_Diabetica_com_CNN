import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import model_from_json
import os

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
    file_bytes = img_input.read()
    np_img = np.frombuffer(file_bytes, np.uint8)
    img_orig = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
    img_cp = img_orig.copy()

    img = img_orig / 255
    img = cv2.resize(img, (224,224))
    img = np.expand_dims(img, 0)

    st.write("Imagem Enviada:")
    st.image(img_orig, caption='Imagem enviada', use_column_width=False, width=200)

    # Realizar a previsão
    # st.write("Fazendo previsão...")
    model = load_model(file_path_json, file_path_weigths)
    prediction_pct = model.predict(img)
    prediction = np.argmax(prediction_pct, axis=1)[0]


    # Exibir a imagem editada com o diagnóstico sobreposto
    st.write("Imagem com Diagnóstico:")
    
    # Lógica para interpretar a previsão e exibir o diagnóstico
    if prediction == 0:  
        cv2.putText(img_cp, 'DR: Positive', (140,220), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,0), 1)
        st.image(img_cp, caption='Diagnóstico sobreposto', use_column_width=False, width=500)
        st.write("Diagnóstico:")
        st.markdown(f'Paciente com<span style="color: red;"> Retinopatia Diabética</span> com {(prediction_pct[0][prediction]):.2%}.', unsafe_allow_html=True)
    else:
        cv2.putText(img_cp, 'DR: Negative', (140,220), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,0), 1)
        st.image(img_cp, caption='Diagnóstico sobreposto', use_column_width=False, width=500)
        st.write("Diagnóstico:")
        st.markdown(f'Paciente<span style="color: blue;"> Normal</span> com {(prediction_pct[0][prediction]):.2%}.', unsafe_allow_html=True)

