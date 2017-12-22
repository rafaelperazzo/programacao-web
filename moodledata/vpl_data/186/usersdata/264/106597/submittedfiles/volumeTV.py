 -*- coding: utf-8 -*-
v= int(input('Digite o volume inicial:'))
t= int(input('Digite a quantidade de trocas:'))

for i in range (0,t,1):
    A= int(input('Digite a quantidade de trocas de volume:'))
    if v+A>100:
        v=100
    elif v+A<0:
        v=0
    else:
        v= v+A
        
print (v)