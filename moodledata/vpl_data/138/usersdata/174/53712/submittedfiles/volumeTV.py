 -*- coding: utf-8 -*-
 v=int(input('Volume inicial:'))
 t=int(input('Quantidade de trocas de volume:'))
 vol=v
 cont=0
 for i in range(1,t+1,1):
     a=int(input('Modificação do volume:'))
     vol=vol+a
     if vol>100:
         vol=100
    if vol<0:
        vol=0
print (vol)