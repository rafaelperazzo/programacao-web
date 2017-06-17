# -*- coding: utf-8 -*-
def maiorDegrau(lista):
    for i in range(0,len(lista),1):
        if ABS(lista[i]-lista[i+1) > ABS(lista[i+1]-lista[i+2])
            resultado=ABS(lista[i]-lista[i+1])
    return (resultado)
        
n=int(input('Informe a quantidade de termos: '))
lista=[]
for i in range(0, n, 1):
    elemento=int(input('Digite os elementos da lista: '))
    lista.append(elemento)

resultadoFinal=maiorDegrau(lista)
print(resultadoFinal)