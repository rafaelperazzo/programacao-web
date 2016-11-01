# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Insira a Quantidade de Notas: ")
t=[]
soma=0

#entrada de valores
for i in range (0,n,1): 
    t.append(input("Digite um Valor: "))

#media
for j in range(0,n,1):
    soma =soma+t[j]
media=soma/n

#desviopadrao
somas=0
for k in range(0,n,1):
    p=(t[k]-media)**2
    somas=somas+p

s=(somas/(n-1))**0.5

#saidas
print("%.2f" %t[0])
print("%.2f" %t[n-1])
print("%.2f" %media)
print t