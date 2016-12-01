# -*- coding: utf-8 -*-
from __future__ import division

n=input("Insira a Quantidade de Salas: ")
a=[]
for i in range(0,n,1):
    a.append(input("Insira a Quantidade de Vidas da Sala: "))
    
entrada=input("Insira a Entrada: ")
saida=input("Insira a Saída: ")

def vidas(a,entrada,saida):
    soma=0
    for i in range(entrada,saida+1,1):
        soma=soma+a[i]
    return soma
    
print vidas(a,entrada,saida)