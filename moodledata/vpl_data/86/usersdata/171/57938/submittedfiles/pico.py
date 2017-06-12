# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1] and lista[i]<lista[i-1]:
            cont=cont+1
            if cont==0:
                return False
            else:
                return True
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
lista=[ ]
for i in range(1,n+1,1):
    valor=float(input('digite os valores da lista:'))
    lista.append(valor)
if pico(a):
    print('S')
else:
    print('N')
