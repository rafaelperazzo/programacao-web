# -*- coding: utf-8 -*-

def soma_impar(lista):
    soma=0
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            soma=soma+lista[i]
            cont=cont+1
    return(soma)
        

def soma_par(lista):
    soma2=0
    cont2=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma2=soma2+lista[i]
            cont2=cont2+1
    return(soma2)

def qunt_impar(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            cont=cont+1
    return(cont)

def qunt_par(lista):
    cont2=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            cont2=cont2+1
    return(cont2)
    
    
n=int(input('Quantidade de elementos: '))
lista=[ ]

for i in range(0,n,1):
    valor=float(input('Valor: '))
    lista.append(valor)
    
print(soma_impar(lista))
print(soma_par(lista))
print(quant_impar(lista))
print(quant_par(lista))





