# -*- coding: utf-8 -*-
N=int(input('Digite a quantidade de participantes: '))
P=int(input('Digite a quantidadede pontos necessários: '))
cont=0

for i in range(0,2*N,1):
    
    x=int(input('Digite a quantidade de pontos jogador:'))
    y=int(input('Digite a quantidade de pontos jogador:'))
    
    if (x+y)==P:
        cont=cont+1
print(cont)