import streamlit as st
import tensorflow as tf
import numpy as np

# # Carregar o modelo treinado
# @st.cache(allow_output_mutation=True)
# def load_model():
#     model = tf.keras.models.load_model('seu_modelo_cnn.h5')  # Substitua 'seu_modelo_cnn.h5' pelo caminho do seu modelo
#     return model

# model = load_model()

# # Função para fazer a previsão
# def predict(image):
#     img = np.asarray(image.resize((128, 128)))  # Redimensionar a imagem conforme necessário
#     img = img / 255.0  # Normalizar os valores dos pixels
#     img = np.expand_dims(img, axis=0)  # Adicionar dimensão extra para a previsão
#     prediction = model.predict(img)
#     return prediction

# # Configuração do app Streamlit
# st.title('Diagnóstico de Retinopatia Diabética')
# st.write('Faça o upload de uma imagem para prever o diagnóstico')

# # Upload da imagem
# uploaded_file = st.file_uploader("Escolha uma imagem", type=['jpg', 'jpeg'])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Imagem enviada', use_column_width=True)
#     st.write("")
#     st.write("Fazendo previsão...")

#     # Realizar a previsão
#     prediction = predict(image)

#     # Lógica para interpretar a previsão e exibir o diagnóstico
#     if prediction[0] > 0.5:  # Exemplo de condição, ajuste conforme necessário
#         st.write("Diagnóstico: Retinopatia Diabética")
#     else:
#         st.write("Diagnóstico: Normal")
