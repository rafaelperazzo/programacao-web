 -*- coding: utf-8 -*-
 v=int(input('digite o volume inicial:))
 t=int(input('digite quantas trocas de volume:'))
 volume=v
 cont=0
 for i in range(1,t+1,1):
     md=int(input('digite a mudança de volume:'))
     volume=volume+md
     if (volume>100):
         volume=100
     if (volume<0):
        volume=0
print(volume)