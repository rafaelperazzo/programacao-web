# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de termos da lista: '))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor da lista: '))
    a=[valor]
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
print(i)