# -*- coding: utf-8 -*-
salas=int(input('Digite o número de salas no corredor: '))
lista=[]
for i in range(0,salas,1):
    vidas=int(input('Digite o número de vida garantida pela sala: '))
    lista.append(vidas)
    
entrada=int(input('Digite a sala que o jogador entrou: '))
saida=int(input('Digite a sala que o jogador saiu: '))

soma=0
for i in range(0,saida,1):
    soma=soma+lista[i]
    
print(soma)

