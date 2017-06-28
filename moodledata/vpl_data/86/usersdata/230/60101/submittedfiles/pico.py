# -*- coding: utf-8 -*-

def picomax(lista):
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            return (i)
def pico(lista):
    x=picomax(lista)
    for i in range (x,len(lista)-1,1):
        if a[i]<a[i+1]:
            return False
    return True

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o elemento da lista: '))
    a.append(valor)
    
if pico(a):
    print('S')
else:
    print('N')

