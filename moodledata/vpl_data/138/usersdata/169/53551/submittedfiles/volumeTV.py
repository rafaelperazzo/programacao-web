 -*- coding: utf-8 -*-
v=int(input('Digite o Volume Inicial:'))
t=int(input('Digite o Total de Trocas de Volume:')) 
volume=v
cont=0
for i in range(1,t+1,1):
    md=int(input('Digite a Mudança de Volume:')) 
    volume=volume+md
    if (volume>100):
        volume=100
    if (volume<0):
        volume=0
print(v)
