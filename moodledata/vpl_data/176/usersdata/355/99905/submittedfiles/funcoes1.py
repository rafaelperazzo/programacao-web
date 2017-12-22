# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,n,1):
        if ((lista[i])<(lista[i+1])):
            cont=cont+1
    if cont>0:
        return('S')
    else: 
        return('N')

#escreva as demais funções
def consec(lista):
    cont=0
    for i in range(0,n,1):
        if ((lista[i])==(lista[(i+1)])):
            cont=cont+1
    if cont>0:
        return('S')
    else: 
        return('N')


def decrescente(lista):
    cont=0
    for i in range(0,n,1):
        if ((lista[i])>(lista[(i+1)])):
            cont=cont+1
    if cont>0:
        return('S')
    else: 
        return('N')

#escreva o programa principal
n=int(input('Digite o tamanho da lista: '))

lista0=[]
print('1º lista')
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista0.append(num)
lista1=[]
print('2º lista')
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista1.append(num)
lista2=[]
print('3º lista')
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista2.append(num)
    
#1 lista:
print(crescente(lista0))
print(decrescente(lista0))
print(consec(lista0))

#2 lista:
print(crescente(lista1))
print(decrescente(lista1))
print(consec(lista1))

#3 lista:
print(crescente(lista2))
print(decrescente(lista2))
print(consec(lista2))
        