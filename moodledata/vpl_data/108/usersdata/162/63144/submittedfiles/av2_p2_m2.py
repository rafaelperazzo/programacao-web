# -*- coding: utf-8 -*-
salas=[]
s=int(input('Digite a quantidade de salas:'))
for i in range(0,s,1):
    vidas=int(input('Digite a quantidade de vidas:'))
    salas.append(vidas)
portaentrada=int(input('Digite a porta de entrada:'))
portasaida=int(input('Digite a porta de saída:'))
soma=0
for i in range(portaentrada,portasaida+1,1):
    soma=soma+1
print(soma)    

