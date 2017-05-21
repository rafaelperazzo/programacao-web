# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o numero de pessoas:'))
soma=0
for i in range(1,n+1,1):
    idade=int(input('digite a idade:'))
    soma=soma+idade
    media=soma/n
print('%d'%media)