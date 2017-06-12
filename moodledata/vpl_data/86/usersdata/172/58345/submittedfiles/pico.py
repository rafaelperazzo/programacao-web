# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    c=0
for i in range(0,len(lista),1):
    if lista[i]>lista[i-1] and lista[i+1]<lista[i]:
        c=c+1
    elif lista[i]>lista[i-1] and lista[i]<lista[i-1]:
    c=c+1
    if cont==0:
        return False
    else: 
        return True
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
lista[]
for i in range(1,n+1,1):
    v=float(input(' valor da lista: '))
    lista.append(v)
if pico(lista):
    print('N')
else:
    print('S')