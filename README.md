Diagnóstico de Retinopatia Diabética com CNN
==============================

**Sobre o conjunto de dados:**\
A prevalência da Retinopatia Diabética é alarmantemente elevada, afetando uma proporção significativa de indivíduos com diabetes de longa data. A detecção precoce e o tratamento oportuno são cruciais para prevenir a perda de visão e melhorar os resultados dos pacientes. No entanto, a interpretação manual de imagens da retina para o rastreio da Retinopatia Diabética pode ser demorada e sujeita a erros humanos. Portanto, há uma necessidade premente de uma ferramenta automatizada e precisa que possa auxiliar os profissionais de saúde na classificação da gravidade da Retinopatia Diabética.
Os métodos existentes para detectar e classificar a Retinopatia Diabética baseiam-se frequentemente em avaliações subjectivas e extenso trabalho manual, levando a ineficiências e potenciais inconsistências no diagnóstico. Além disso, a crescente prevalência da diabetes e a disponibilidade limitada de oftalmologistas agravam ainda mais os desafios no rastreio e diagnóstico atempados. Portanto, há necessidade de desenvolver um sistema automatizado robusto e confiável que possa detectar e classificar com precisão a Retinopatia Diabética, permitindo intervenção precoce e planos de tratamento personalizados.

**Descrição de dados :**\
Este conjunto de dados consiste em uma grande coleção de imagens retinais de alta resolução capturadas sob várias condições de imagem. Um profissional médico avaliou a presença de Retinopatia Diabética em cada imagem e atribuiu uma classificação numa escala que varia entre 0 e 1, que corresponde às seguintes categorias:

<font color='red'> **Retinopatia Diabética ---> 0**\
<font color='lightgreen'> **Sem Retinopatia Diabética ---> 1**


Organização do Projeto:
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
