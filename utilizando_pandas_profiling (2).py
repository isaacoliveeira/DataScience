# -*- coding: utf-8 -*-
"""Utilizando Pandas Profiling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14VHsIDPNdsLgnoQkM5ECEyVqbjrUG_wU

# Curso Udemy

Variáveis - Numericas [Continua(numeros reais) e Discreta(conjunto de valores continuas)] e Categóricas(String)  [Nominal(dados não mensuráveis/ sem ordenação) e ordinal(sob ordem)]

Utilizando a base de dados de credito
"""

#!pip install plotly --upgrade

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('/content/credit_data.csv')

base_credit

quantidade_default_0 = base_credit[base_credit['default'] == 0].shape[0]
quantidade_default_0

quantidade_default_1 = base_credit[base_credit['default'] == 1].shape[0]
quantidade_default_1

np.unique(base_credit['default'], return_counts=True)

sns.countplot(x = base_credit['default']); #gerar graficos

plt.hist(x = base_credit['age']); #gerar histogramas

plt.hist(x = base_credit['income']);

plt.hist(x = base_credit['loan']);

grafico  = px.scatter_matrix(base_credit, dimensions=['age', 'income','loan'], color='default')
grafico

"""Correção de alguns dados"""

base_credit[base_credit['age']  < 18.1]

base_credit.describe()

base_credit.head(30)

base_credit.loc[pd.isna(base_credit['age'])]

base_credit.loc[pd.isna(base_credit['age']), 'age'] == 42

base_credit.loc[pd.isna(base_credit['age'])]

base_credit.head(35)

base_credit.isnull().sum()

base_credit.loc[(base_credit['clientid'] == 29) | (base_credit['clientid'] == 31) | (base_credit['clientid'] == 32)]

base_credit.loc[base_credit['clientid'].isin([29,31,32])]

X_cred = base_credit.iloc[:,1:4].values
X_cred

type(X_cred)

Y_cred = base_credit.iloc[:,4].values
Y_cred

"""#Escalonamento#"""

X_cred

X_cred[:, 0].max(), X_cred[:, 1].max(), X_cred[:, 2].max()

X_cred[:, 0].min(), X_cred[:, 1].min(), X_cred[:, 2].min()

from sklearn.preprocessing import StandardScaler
#padronizar
scaler_credit = StandardScaler()
X_cred = scaler_credit.fit_transform(X_cred)

X_cred[:, 0].min(), X_cred[:, 1].min(), X_cred[:, 2].min()

X_cred[:, 0].max(), X_cred[:, 1].max(), X_cred[:, 2].max()

X_cred

"""#Utilizando a base de dados do censo

"""

base_census = pd.read_csv('census.csv')

base_census

base_census.describe()

base_census.isnull().sum()

np.unique(base_census['income'], return_counts=True)

sns.countplot(x = base_census['income']);

plt.hist(x = base_census['age']);

plt.hist(x = base_census['education-num'])

plt.hist(x = base_census['hour-per-week']);

grafico = px.treemap(base_census, path=['workclass', 'age']);
grafico.show()

grafico = px.treemap(base_census, path=['occupation', 'relationship','age', 'income']);
grafico.show()

grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'])
grafico.show()

grafico = px.parallel_categories(base_census, dimensions=['education', 'income'])
grafico.show()

"""#divisões entre previsores e classe"""

base_census.columns

X_census = base_census.iloc[:, 0:14].values
X_census

X_census[0]

y_census = base_census.iloc[:, 14].values
y_census

"""#Tratamento de atributos categoricos

"""

from sklearn.preprocessing import LabelEncoder
label_enconder_test = LabelEncoder()

teste = label_enconder_test.fit_transform(X_census[:, 1]) #transforma de string para inteiro

X_census[:, 1]

teste

label_enconder_workclass = LabelEncoder()
label_enconder_education = LabelEncoder()
label_enconder_marital = LabelEncoder()
label_enconder_occupation = LabelEncoder()
label_enconder_relationship = LabelEncoder()
label_enconder_race = LabelEncoder()
label_enconder_sex = LabelEncoder()
label_enconder_country = LabelEncoder()

X_census[0]

X_census[:, 1] = label_enconder_workclass.fit_transform(X_census[:, 1])
X_census[:, 3] = label_enconder_education.fit_transform(X_census[:, 3])
X_census[:,5] = label_enconder_marital.fit_transform(X_census[:,5])
X_census[:,6] = label_enconder_occupation.fit_transform(X_census[:,6])
X_census[:,7] = label_enconder_relationship.fit_transform(X_census[:,7])
X_census[:,8] = label_enconder_race.fit_transform(X_census[:,8])
X_census[:,9] = label_enconder_sex.fit_transform(X_census[:,9])
X_census[:, 13] = label_enconder_country.fit_transform(X_census[:, 13])

base_census

X_census[1]


