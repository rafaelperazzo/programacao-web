# -*- coding: utf-8 -*-
n=int(input('Digite o número de salas:'))
v=[]
for i in range(1,n+1,1):
    Porta=int(input('Digite o número da porta:'))
    v.append(Porta)
    
P1=int(input('Porta de entrada:'))
P2=int(input('Porta de saída:'))
soma=0
for j in range(P1,P2+1,1):
    soma=soma+v[j]
    
print(soma)

