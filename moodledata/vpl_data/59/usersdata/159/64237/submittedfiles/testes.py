# -*- coding: utf-8 -*-
import numpy as np

#Essa função tem como parametros os graus, minutos e segundos de um ângulo sexasimal e retorna o ângulo em decimais
def angulo(g,m,s):
    angulom=m/60
    angulos=s/3600
    soma=g+angulom+angulos
    
    return soma

#Essa função transforma ângulos decimais, contidos em uma lista, em ângulos sexasimais, agrupando-os em uma matriz de 3 colunas, que são respectivamente os graus, minutos e segundos de cada ângulo. Com n ângulos distribuídos pelas linhas
def graus (azi):
    a=np.zeros((len(azi),3))
    for i in range (0,len(azi),1):
        g=int(azi[i])
        b=azi[i]-g
        c=b*60
        m=int(c)
        j=c-m
        s=j*60
        a[i,0]=g
        a[i,1]=m
        a[i,2]=s
    return a

#Essa função calcula o azimute de todos os pontos de acordo com a fórmula    
def azimute (angulo,d):
    azi=[]
    for i in range (0,len(d),1):
        azimute=angulo+d[i]
        azi.append(azimute)
        angulo=azimute
    return (azi)
    
g=int(input('Graus do primeiro azimute:'))
m=int(input('Minutos do primeiro azimute:'))
s=int(input('Segundos do primeiro azimute:'))
n=int(input('Número de deflexões:'))

#Criou-se uma lista para armazenar as deflexões.
d=[]
for i in range (0,n,1):
    deflexao=float(input('Deflexão:'))
    d.append(deflexao)

#Depois de receber as entradas, transformamos os dados do primeiro azimute para decimal.
primeiroazi=(angulo(g,m,s))

azimutes=azimute(primeiroazi,d)

print(graus(azimutes))

