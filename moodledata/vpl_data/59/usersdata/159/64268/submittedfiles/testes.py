# -*- coding: utf-8 -*-
import numpy as np

#Essa função tem como parametros os graus, minutos e segundos de um ângulo sexasimal e retorna o ângulo em decimais
def angulo(g,m,s):
    angulom=m/60
    angulos=s/3600
    soma=g+angulom+angulos
    
    return soma

'''
Essa função transforma ângulos decimais, contidos em uma lista, em ângulos sexasimais, agrupando-os em uma matriz de 3 colunas, 
que são respectivamente os graus, minutos e segundos de cada ângulo. Com n ângulos distribuídos pelas linhas
'''

def graus (azi):
    a=np.zeros((len(azi),3))
    for i in range (0,len(azi),1):
        graus=int(azi[i])
        b=azi[i]-graus
        c=b*60
        minutos=int(c)
        j=c-minutos
        segundos=j*60
        a[i,0]=graus
        a[i,1]=minutos
        a[i,2]=segundos
    return a

#Essa função calcula o azimute de todos os pontos de acordo com a fórmula Azi=Azi-1+Dei  
def azimute (angulo,dei):
    azi=[]
    for i in range (0,len(dei),1):
        azimute=angulo+dei[i]
        azi.append(azimute)
        angulo=azimute
    return (azi)
    
g=int(input('Graus do primeiro azimute:'))
m=int(input('Minutos do primeiro azimute:'))
s=int(input('Segundos do primeiro azimute:'))
n=int(input('Número de deflexões:'))

#Criou-se uma lista para armazenar as deflexões.
dei=[]
for i in range (0,n,1):
    deflexao=float(input('Deflexão:'))
    dei.append(deflexao)

#Depois de receber as entradas, transformamos os dados do primeiro azimute para decimal.
primeiroazi=(angulo(g,m,s))

#Aplicando na função o primeiro azimute e a lista de deflexões obtemos uma lista com os azimutes (em decimais) em todos os pontos
azimutes=azimute(primeiroazi,dei)

#Aplicar a lista com os valores do azimute (em decimais) e transformar em uma matiz com 3 colunas que são graus, minutos e segundos, respectivamente 
print(graus(azimutes))

