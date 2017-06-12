 -*- coding: utf-8 -*-
a=int(input('Digite o volume inicial'))
b=int(input('Digite a mudanca do volume:'))
soma=a
for i in range(1,b+1,1):
    c=int(input('Digite a alteracao do volume:'))
    soma=soma+c
    if soma>100:
        soma=100
    elif soma<0:
        soma=0
print(soma)