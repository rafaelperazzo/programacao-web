# -*- coding: utf-8 -*-

def soma_impar(lista):
    soma=0
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            soma2=soma2+lista[i]
            cont2=cont2+1
    return(soma)
        


def soma_par(lista):
    soma2=0
    cont2=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+lista[i]
            cont=cont+1
    return(soma2)




n=int(input('Quantidade de elementos: '))
lista=[ ]

for i in range(0,n,1):
    valor=float(input('Valor'))
    lista.append(valor)
    
print(soma_impar)
print(soma_par)
print(cont)
print(cont2)