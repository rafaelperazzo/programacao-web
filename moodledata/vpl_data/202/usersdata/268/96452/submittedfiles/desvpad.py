# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite o numero de termos : '))
a=[]
soma=0

for i in range(0,n,1):
    valor=int(input('Digite o termo :'))
    a.append(valor)
    soma=soma+valor
media=soma/len(a)

