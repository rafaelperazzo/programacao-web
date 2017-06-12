# -*- coding: utf-8 -*-
n=int(input('digite o número de n:'))
p=int(input('digite o número de p:'))
pontos=0
cont=0

for i in range (1, n+1, 1):
    x=int(input('digite o valor de x:'))
    y=int(input('digite o valor de y:'))
    ponto=x+y
    if ( pontos>=p):
        cont=cont+1
print ( cont)