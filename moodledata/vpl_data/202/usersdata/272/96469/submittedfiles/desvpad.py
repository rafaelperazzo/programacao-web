# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite o número de termos: '))
a=[]
for i in range(0,n,1):
    a.append(int(input('Digite o valor: ')))
soma=0
for j in range(0,len(a),1):
    soma=soma+a[j]
media=soma/len(a)

    