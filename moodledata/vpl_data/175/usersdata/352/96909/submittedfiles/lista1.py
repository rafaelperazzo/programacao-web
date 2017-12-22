# -*- coding: utf-8 -*-


def soma_par(lista):
    soma=0
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+lista[i]
            cont=cont+1
    return(soma)

def soma_impar(lista):
    soma=0
    cont2=cont2+1
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            soma=soma+lista[i]
        return(soma)


n=int(input('Quantidade de elementos: '))
lista=[ ]

for i in range(0,n,1):
    valor=float(input('Valor'))
    lista.append(valor)
