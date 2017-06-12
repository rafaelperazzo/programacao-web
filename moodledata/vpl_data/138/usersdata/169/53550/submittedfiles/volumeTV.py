 -*- coding: utf-8 -*-
v=int(input('Digite o Volume Inicial:'))
t=int(input('Digite o Total de Trocas de Volume:')) 
v=volume
cont=0
for i in range(1,t+1,1):
    md=int(input('Digite a Mudança de Volume:')) 
    v=volume+md
    if (v>100):
        v=100
    if (v<0):
        v=0
print(v)
