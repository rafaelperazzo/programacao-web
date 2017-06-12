# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores: '))
lista = []
for i in range (1,n+1,1):
    valor = input('Digite o valor '+str(i)+': ')
    lista.append(valor)

def impares (lista):
    contI=0
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            soma=soma+lista[i]
            contI=contI+1
    return(contI,soma)
    
print(lista.impares(lista))



