# -*- coding: utf-8 -*-
N=int(input('Digite o número de competidores: '))
P=int(input('Digite o número mínimo de pontos para ser convidado: '))
cont=0
for i in range(1,N+1,1):
    x=int(input('Digite a primeira pontuação: '))
    y=int(input('Digite a segunda pontuação: '))
    pontuação=x+y
    if pontuação>=P:
        cont=cont+1
print(cont)        