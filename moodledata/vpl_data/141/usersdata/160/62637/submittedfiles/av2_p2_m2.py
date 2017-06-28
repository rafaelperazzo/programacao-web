# -*- coding: utf-8 -*-

sala=int(input('Digite a quantidade de salas:'))

vida=[]
for in in range(0,sala,1):
    valor=int(input('Digite a vida dessa sala:'))
    vida.append(valor)
    
entrada=int(input('Digite a porta de entrada:'))
saida=int(input('Digite a porta de saída:'))

soma=0
for i  in range(entrada,saida+1,1):
    soma=soma+vida[i]
print(soma)