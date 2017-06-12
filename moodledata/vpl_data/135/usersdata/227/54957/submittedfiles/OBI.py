# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de competidores:'))
p=int(input('Digete o numero de pontos para ser convidado:'))
pontos=0
cont=0
for i in range (1,n+1,1):
    x=int(input('digite o numero de pontos da primeira fase:'))
    y=int(input('digite o numero de pontos da segunda fase:'))
    pontoa=x+y
    if(pontos>=p):
        cont=cont+1
print(cont)