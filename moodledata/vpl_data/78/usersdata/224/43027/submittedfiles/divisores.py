# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quatidade de divisores a ser mostrados: '))
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundoo valor: '))
cont=0
v1=0
v2=0
soma=0
for i in range(1,n+1,1):
    v1=v1+a*i
    v2=v2+b*i
    if v1==v2:
        soma=soma+1
    else:
        cont=cont+2
    print(soma)
    print(cont)