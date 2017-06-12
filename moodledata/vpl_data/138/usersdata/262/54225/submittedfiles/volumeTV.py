 -*- coding: utf-8 -*-
 
vol=int(input('Digite o Volume Inicial:'))
tv=int(input('Digite o Total de Trocas de Volume:'))
volume=vol
cont=0
for i in range(1,tv+1,1):
    mv=int(input('Digite a Mudança de Volume:'))
    volume=volume+mv
    if(volume>100):
        volume=100
    if(volume<100):
        volume=0
print(volume)