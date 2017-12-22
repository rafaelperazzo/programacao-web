 -*- coding: utf-8 -*-
 
 volume1=int(input('volume inicial:'))
 trocas= int(input('número de trocas de volumes feitas:'))
 for i in range (0,trocas,1):
     nut=int(input('troca feita:'))
     volume1=volume1+nut
     if volume1>100:
        volime1=100
    elif volume1<0:
        volume1=0
print (volume1)
        
    