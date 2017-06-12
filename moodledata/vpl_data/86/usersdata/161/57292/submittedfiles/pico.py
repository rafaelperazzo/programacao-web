# -*- coding: utf-8 -*-
n =int(input('Digite a quantidade de elementos da lista: '))
lista=[]
for i in range(0,n,1):
    numero=float(input('Informe um número:'))
    lista.append(numero)
    
def pico(lista):
    cont=0
    for i in range(1,len(lista)/2,1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
     for i in range(len(lista)/2, len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False


if pico(lista):
    print('S')
else:
    print('N')
    