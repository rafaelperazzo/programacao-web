# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    for i in range(1,(len(lista)-1)/2,1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    for i in range((len(lista)-1)/2,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
lista=[]
for i in range(1,n+1,1):
    v=float(input('Digite o valor:'))
    lista.append(v)
if pico(lista):
    print('S')
else:
    print('N')