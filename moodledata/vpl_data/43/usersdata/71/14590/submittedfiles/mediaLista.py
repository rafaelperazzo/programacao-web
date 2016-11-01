# -*- coding: utf-8 -*-
from __future__ import division

n = input("Insira a Quantidade de Notas: ")
t=[]

#entrada de valores
for i in range (0,n,1): 
    t.append(input("Digite um Valor: "))

soma=0
for j in range(0,n,1):
    soma =soma+t[j]