# -*- coding: utf-8 -*-
n=int(input('digite o número de salas :'))
lista=[]
for i in range(0,len(lista),1):
    vidas=int(input('digite o valor das vidas da sala :'))
    lista.append(vidas)

entrada=int(input('digite o número da porta de entrada :'))   
saida=int(input('digite o número da porta de saida :'))

soma=0
for i in range(entrada,saida,1):
    soma=soma+lista[i]

resultado=soma
print(resultado)
