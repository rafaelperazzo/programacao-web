# -*- coding: utf-8 -*-
from __future__ import division

n = input("Insira a Quantidade de Notas: ")
t=[]
soma=0

#entrada de valores
for i in range (0,n,1): 
    t.append(input("Digite um Valor: "))

for j in range(0,n,1):
    soma =soma+t[j]
    
