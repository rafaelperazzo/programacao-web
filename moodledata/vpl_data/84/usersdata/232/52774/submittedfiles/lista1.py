# -*- coding: utf-8 -*-
def somaimpar(lista):
    soma=0
    for i in range (0,len(lista),1):
        if lista[i]%2!=0:
            soma=soma+i
    return soma

def somapar(lista):
    soma=0
    for i in range (0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+i
    return soma
    
def qimpar(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i%2!=0:
            cont=cont+1
    return cont

def qpar(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i%2==0:
            cont=cont+1
    return cont

lista=[ ]
n=int(input('Digite o número de elementos da lista: '))
for i in range (1,n+1,1):
    a=int(input('Digite o valor do elemento da lista: '))
    lista.append(lista)

print(somaimpar(lista))
print(somapar(lista))
print(qimpar(lista))
print(qpar(lista))

