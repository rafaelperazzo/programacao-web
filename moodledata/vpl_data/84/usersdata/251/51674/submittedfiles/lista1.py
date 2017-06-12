# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores: '))
lista = []
for i in range (1,n+1,1):
    valor = int(input('Digite o valor '+str(i)+': '))
    lista.append(valor)

def impares (lista):
    contI=0
    somaI=0
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            somaI=somaI+lista[i]
            contI=contI+1
    return(contI,somaI)
    
def pares (lista):
    contP=0
    somaP=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            somaP=somaP+lista[i]
            contP=contP+1
    return(contP,somaP)    




print(impares(lista)[1])
print(pares(lista)[1])
print(impares(lista)[0])
print(pares(lista)[0])


