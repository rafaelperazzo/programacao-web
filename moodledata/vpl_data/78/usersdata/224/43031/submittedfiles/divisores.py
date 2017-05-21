# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quatidade de divisores a ser mostrados: '))
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundoo valor: '))
soma=0
cont=0
i=1
for i in range(1,n+1,1):
    soma=soma+a*i
    soma=soma+b*i
    i=i+1
