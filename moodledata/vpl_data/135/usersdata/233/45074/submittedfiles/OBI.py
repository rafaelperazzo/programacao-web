# -*- coding: utf-8 -*-
n=int(input('Digite o número de competidores: '))
p=int(input('Digite o número mínimo de pontos para ser convidado: '))
cont=0
for i in range(1,n+1,1):
    x=int(input('Digite a primeira pontuação: '))
    y=int(input('Digite a segunda pontuação: '))
    pontuação=x+y
    if pontuação>=p:
        cont=cont+1
print(cont)        