# -*- coding: utf-8 -*-

competidores1=int(input('Digite a quantidade de competidores:'))
competidores2=int(input('Digite a quantidade de competidores:'))

cont=0
for i in range(1,competidores1+1,1):
    pontos1=int(input('Digite a quantidade de pontos da 1° prova:'))
    pontos2=int(input('Digite a quantidade de pontos da 2° prova:'))
    if (pontos1+pontos2)>=competidores2:
        cont=cont+1
print(cont)