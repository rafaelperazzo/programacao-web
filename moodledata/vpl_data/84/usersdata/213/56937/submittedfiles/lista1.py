# -*- coding: utf-8 -*-
n=int(input('Informe o número de termos: '))
lista=[]
for i in range(0, n, 1):
    elemento=int(input('Informe os termos da lista: '))
    lista.append(elemento)

somaImpar=0
contadorImpar=0
somaPar=0
contadorPar=0
for i in range(0, len(lista), 1):
    if (lista[i]%2)==0:
        somaPar=somaPar+lista[i]
        contadorPar=contadorPar+1
    else:
        somaImpar=somaImpar+lista[i]
        contadorImpar=contadorImpar+1

print(somaImpar)
print(somaPar)
print(contadorImpar)
print(contadorPar)
print(lista)