# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Definindo a Função
#Para o valor do indice da Sala de Entrada menor ou igual ao indice da Sala de Saída
def Qvidas1(salas,vidas,entrada,saida):
    soma=0
    for i in range(entrada, saida+1,1):
        soma=soma+vidas[i]
    return soma
    
#Para o valor do indice da Sala de Entrada maior que o indice da Sala de Saída
def Qvidas2(salas,vidas,entrada,saida):
    soma=0
    for i in range(saida, entrada+1,1):
        soma=soma+vidas[i]
    return soma
    
#Entrada
salas=input('Digite a Quantidade de salas: ')
vidas=[]

for i in range(0,salas,1):
    vidas.append(input('Digite um valor para o número de vidas: '))
    
entrada=input('Digite o indice da sala de entrada: ')
saida=input('Digite o indice da sala de saída: ')

if entrada<=saida:
    print Qvidas1(salas,vidas,entrada,saida)
else:
    print Qvidas2(salas,vidas,entrada,saida)



