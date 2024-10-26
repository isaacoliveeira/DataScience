# -*- coding: utf-8 -*-
"""Utilizando Pandas Profiling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14VHsIDPNdsLgnoQkM5ECEyVqbjrUG_wU
"""

#!pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport

from google.colab import drive
drive.mount('/content/drive')

import os

os.listdir('/content/drive/MyDrive/')

base = pd.read_csv('/content/drive/MyDrive/Pandas/titanic_train.csv')
base

profile = ProfileReport(base, title='Titanic Report')

profile

profile.to_file('/content/titanic_report.html')

import os
print(os.listdir('/content'))

from google.colab import files
files.download('/content/titanic_report.html')