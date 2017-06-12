# -*- coding: utf-8 -*-
n=int(input('digite o número de competidores: '))
p=int(input('digite a pontuação mínima: '))
cont=0
for i in range(1,n+1,1):
    x=int(input('digite o valor da primeira etapa: '))
    y=int(input('digite o valor da segunda etapa: '))
    if x+y>=p:
        cont=cont+1
print(cont)        