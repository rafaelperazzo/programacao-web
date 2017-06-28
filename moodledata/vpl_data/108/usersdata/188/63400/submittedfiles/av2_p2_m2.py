# -*- coding: utf-8 -*-
sal=int(input('Digite a Quantidade de Salas:'))
lista=[]
for i in range(0,sal,1):
    vid=int(input('digite o Quantidade de Vidas:'))
    lista.append(vid)
porte=int(input('Digite a Porta de Entrada:'))
ports=int(input('Digite a Porta de Saída:'))
soma=0
for i in range(porte,ports+1,1):
    soma=soma+lista[i]
print(soma)

