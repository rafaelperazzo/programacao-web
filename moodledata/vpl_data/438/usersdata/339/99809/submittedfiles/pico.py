# -*- coding: utf-8 -*-

def pico(lista):
    soma=0
    for i in range(0,len(lista)):
        if lista[i]<lista[i+1] and lista[i+1]>lista[i+2]:
            soma+=1
        else:
            soma+=0
    if soma==1:
        print('S')
    else:
        print('N')
    return


n = int(input('Digite a quantidade de elementos da lista: '))
a=[]

for i in range(0,n,1):
    a.append(int(input('Elementos para a: ')))
    
pico(a)

#CONTINUE...
