# 👁️ ***Diagnóstico de Retinopatia Diabética com CNN***

Este projeto utiliza Redes Neurais Convolucionais (CNN) para automatizar a detecção de Retinopatia Diabética em imagens de retina de alta resolução, visando auxiliar profissionais de saúde em diagnósticos rápidos e precisos.

## 📋 ***Sobre o Projeto***

A Retinopatia Diabética é uma das principais causas de perda de visão no mundo. A triagem manual é demorada e escassa em muitas regiões. Este sistema automatizado busca:
* Reduzir erros humanos na interpretação de exames.
* Aumentar a escalabilidade do diagnóstico.
* Permitir intervenção precoce, crucial para salvar a visão do paciente.

## 📊 ***O Conjunto de Dados***
As imagens foram classificadas por especialistas em uma escala binária:
* 🔴 0 (Retinopatia Diabética): Presença de alterações patológicas.
* 🟢 1 (Sem Retinopatia Diabética): Retina saudável.
Nota: Para testar a aplicação, utilize as imagens de exemplo localizadas em: src/features/Dr e src/features/not_dr.

## 🛠️ ***Tecnologias e Estrutura***
O projeto segue o padrão Data Science Cookiecutter para melhor organização:
text

├── LICENSE
├── README.md          <- Documentação principal.
├── data/              <- Dados brutos (raw), intermediários e processados.
├── models/            <- Modelos treinados e serializados (.h5, .pkl).
├── notebooks/         <- Exploração de dados e experimentos.
├── src/               <- Código-fonte (scripts de treino, processamento e visualização).
├── requirements.txt   <- Dependências para rodar o projeto.
└── setup.py           <- Torna o projeto instalável via pip.

## 🚀 ***Como Executar***
### 1. Clonar o repositório
git clone https://github.com
cd nome-do-repositorio

### 2. Instalar dependências
bash
pip install -r requirements.txt

### 3. Executar o Web App (Streamlit)
bash
streamlit run app.py

## 📈 ***Resultados***
(Dica: Adicione aqui uma frase sobre a acurácia do seu modelo ou uma imagem/gráfico
