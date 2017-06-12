# -*- coding: utf-8 -*-
n=int(input('Informe o número de elementos:'))
lista1=[]
lista2=[]
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista1.append(numero)
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista2.append(numero)    
def lecker(lista):
    cont=0
    if lista[0]>lista[1]:
        cont=cont+1
    elif lista[len(lista)-1] > lista[len(lista)-2]:
        cont=cont+1
    for i in range(1,len(lista)-1,1):
        if lista[a] > lista[a-1] and lista[a] > lista[a+1]:
            cont=cont+1
    if cont==1:
        return True
    if cont!=1:
        return False
if lecker(lista1):
    print('S')
else:
    print('N')
if lecker(lista2):
    print('S')
else:
    print('N')

    

