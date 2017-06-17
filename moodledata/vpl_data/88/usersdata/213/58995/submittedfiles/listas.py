# -*- coding: utf-8 -*-
def maiorDegrau(lista):
    for i in range(0,len(lista)-2,1):
        if abs(abs(lista[i])-abs(lista[i+1])) > abs(abs(lista[i+1])-abs(lista[i+2])):
            resultado=abs(abs(lista[i])-abs(lista[i+1]))
        else:
            resultado=abs(abs(lista[i+1])-abs(lista[i+2]))
    return (resultado)
        
n=int(input('Informe a quantidade de termos: '))
lista=[]
for i in range(0, n, 1):
    elemento=int(input('Digite os elementos da lista: '))
    lista.append(elemento)

resultadoFinal=maiorDegrau(lista)
print(resultadoFinal)