# -*- coding: utf-8 -*-
l1=int(input('Digite um numero: '))
    4 l2=int(input('Digite um numero: '))
    5 l3=int(input('Digite um numero: '))
    6 l4=int(input('Digite um numero: '))
    7 conjunto=[l1,l2,l3,l4]
    8     #quantidade de numeros maiores que seus vizinhos
    9 nleck = 0
   10 if conjunto [0] > conjunto[1]:
   11     nleck+=1
   12 for i in range (1,3):
   13     if (conjunto[i-1] < conjunto[i]) and (conjunto[i] > conjunto[i+1]):
   14         nleck+=1
   15 if conjunto[3]>conjunto[2]:
   16         nleck+=1
   17 if nleck==1:
   18     print ('S')
   19 else:
   20     print ('N')
