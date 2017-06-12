# -*- coding: utf-8 -*-
n=int(input('digite o numero de competidores:'))
p=int(input('digite a pontuacao minima para ser convidado:'))
i=0
cont=0
for i in range(1,n+1,1):
    a=int(input('digite os pontos da fase 1:'))
    b=int(input('digite os pontos da fase 2:'))
    i=i+1
    if a+b>=p:
        cont=cont+1
print(cont)