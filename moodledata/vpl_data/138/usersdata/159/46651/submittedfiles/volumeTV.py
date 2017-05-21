# -*- coding: utf-8 -*-
v=int(input('Volume inicial:'))
t=int(input('Número de trocas:'))
contador=v

for i in range (1,t+1,1):
    a=int(input('Modificação de volume:'))
    contador=contador+a
    if contador>100:
        contador=100
    elif contador<0:
        contador=0
print(contador)        
