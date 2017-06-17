# -*- coding: utf-8 -*-
def maiorDegrau(lista):
    resultado=abs(lista[0]-lista[1])
    for i in range(0,len(lista)-1,1):
        if abs(lista[i]-lista[i+1]) > resultado:
            resultado=abs(lista[i]-lista[i+1])
    return (resultado)
        
n=int(input('Informe a quantidade de termos: '))
lista=[]
for i in range(0, n, 1):
    elemento=int(input('Digite os elementos da lista: '))
    lista.append(elemento)

resultadoFinal=maiorDegrau(lista)
print(resultadoFinal)