# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de competidores: '))
p=int(input('digite a pontuação mínima:'))
cont=0
for i in range(1,n+1,1):
    a=int(input('Digite o valor da primeira etapa:'))
    b=int(input('Digite o valor da segunda etapa:'))
    if a+b>=p:
        cont=cont+1
print(cont)