 -*- coding: utf-8 -*-
v= int(input('Digite o volume inicial:'))
t= int(input('Digite a quantidade de trocas:'))

for i in range (0,t,1):
    A_i= int(input('Digite a quantidade de trocas de volume:'))
    if v+A_i>100:
        v=100
    elif v+A_i<0:
        v=0
    else:
        v= v+A_i
        
print (v)