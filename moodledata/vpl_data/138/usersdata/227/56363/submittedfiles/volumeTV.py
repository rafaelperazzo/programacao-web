 -*- coding: utf-8 -*-
 
 v=int(input('Digite o volume incial:'))
t=int(input('digite o numero de mudanças de volume:'))
volume=0
cont=0
for i in range (1,n+1,):
    a=int(input('Digite a mudança de volume:'))
    volume=volume+a
    if (volume>100):
        volume=100
    if (volume<0):
        volume=0
print(volume)