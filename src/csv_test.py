#   Autor: Moacir Werter 
#   Coloque o código numa pasta chamada /src e os arquivos de saída em /results.
#   Python 3.7.7

import csv
import pandas as pd 
import numpy
import numpy as np
import collections
from collections import defaultdict
import statistics 
from statistics import mode 

# 1 - Faça um código em python3 que leia o arquivo data.csv;

data = pd.read_csv('../data/data.csv', skiprows=4)
print(data)

# 2 - Salve em um arquivo .csv o first_name e o gender de cada pessoa. 
# E imprimar na tela a média das idades;

df = pd.read_csv('../data/data.csv', usecols=['first_name', 'gender'])
print(df)

#Salve
df.to_csv('../data/df.csv')

#Média
age = pd.read_csv('../data/data.csv', usecols=['age'])
print(age)
media = age.mean()
print(media)

#3 - Salve em um arquivo .csv o nome completo das últimas 50 pessoas. E imprima alguma informação que você ache interessante.

name = pd.read_csv('../data/data.csv', usecols=['first_name','last_name'])
df = pd.DataFrame(data=name)
name50 = df[-51:]

#Salve
name50.to_csv('../data/name50.csv')

#Informação 
print("I deserve the opportunity!")

#4 - Salve em um arquivo txt o gênero e idade que mais se repete.

repet = pd.read_csv('../data/data.csv', usecols=['gender','age'])
df1 = pd.DataFrame(data=name)

a = repet['age'].value_counts()
print(a)

b = repet['gender'].value_counts()
print(b)

gendage = [a,b]
print(gendage)

#Salve
file = open("../data/gendage.txt","w") 
file.write(gendage)
file.close()
