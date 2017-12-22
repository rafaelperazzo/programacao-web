 -*- coding: utf-8 -*-
 V= int(input('Digite o volume inicial:'))
 T= int(input('Digite a quantidade de trocas:'))

for i in range (0,T,1):
    A= int(input('Digite a quantidade de trocas de volume:'))
    if V+A>100:
        V=100
    elif v+A<0:
        V=0
    else:
        V= V+A
        
print (V)