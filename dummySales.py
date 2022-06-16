# coding: utf-8
import pandas as pd
import matplotlib.pyplot as grafico
import numpy as np

arquivo = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/dummySales/Dummy Data HSS.csv")
arquivo["TV"].fillna(0,inplace=True)
arquivo["Radio"].fillna(0,inplace=True)
arquivo["Social Media"].fillna(0,inplace=True)
arquivo.dropna(inplace=True)
arquivo["Indice"] = arquivo.index + 0
arquivo["Investimento"] = arquivo["TV"] + arquivo["Radio"] + arquivo["Social Media"]
arquivo["Rentabilidade"] = ((arquivo["Sales"] / (arquivo["TV"] + arquivo["Radio"] + arquivo["Social Media"])))*100

""" teste = open("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/dummySales/paraDashboard.csv","a")
for i in range(0,len(arquivo),1):
    #if arquivo.iloc[i,4] == 0: continue
    teste.write("\n")
    teste.write(str(round(arquivo.iloc[i,0]*1000000,2)))
    teste.write(",")
    teste.write(str(round(arquivo.iloc[i,1]*1000000,2)))
    teste.write(",")
    teste.write(str(round(arquivo.iloc[i,2]*1000000,2)))
    teste.write(",")
    teste.write(arquivo.iloc[i,3])
    teste.write(",")
    teste.write(str(round(arquivo.iloc[i,4]*1000000,2)))
    teste.write(",")
    teste.write(str(round(arquivo.iloc[i,6]*1000000,2)))
    teste.write(",")
    teste.write(str(round(arquivo.iloc[i,7],2)))
teste.close() """

campanhaMaisRentavel = arquivo.iloc[183,:]
print(campanhaMaisRentavel)

#print(round(arquivo.iloc[2,1]*1000000,2))

macro = arquivo[arquivo["Influencer"] == "Macro"]
micro = arquivo[arquivo["Influencer"] == "Micro"]
mega = arquivo[arquivo["Influencer"] == "Mega"]
nano = arquivo[arquivo["Influencer"] == "Nano"]

""" grafico.boxplot([macro["Rentabilidade"],micro["Rentabilidade"],mega["Rentabilidade"],nano["Rentabilidade"]])
grafico.grid()
grafico.show() """

#print(arquivo.corr()["Sales"].sort_values(ascending=True))

""" print(macro["Sales"].describe())
print(micro["Sales"].describe())
print(mega["Sales"].describe())
print(nano["Sales"].describe()) """

""" print(len(macro))
print(len(micro))
print(len(mega))
print(len(nano)) """

""" grafico.scatter(arquivo["Investimento"],arquivo["Sales"])
grafico.xlabel("total investido")
grafico.ylabel("total vendas")
grafico.grid()
grafico.show() """

""" 
Questões
Qual campanha mais rentável ? 
R: 3359,31% de retorno. Essa campanha teve um investimento inferior a 2 milhões e retorno superior a 50 milhões.

Qual variável mais influenciou as vendas ?
R: TV com coeficiente de correlação igual a 0,99. Quanto maior o investimento em TV, maior as vendas.

O tipo de influencer não influencia no total de vendas ou na rentabilidade.
"""