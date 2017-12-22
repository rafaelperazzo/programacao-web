# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    som = 0
    i = 0
    j = 0
    b=999
    while True:
        if lista[i+1]>lista[i] and lista[i+1]<lista[i+2]:
            b = lista[i+1]
            j = i+2
            i +=1
        else:
            break
    for k in range (j+1,n,1):
            if b>lista[k]:
                som +=1
    if som == 0 :
        print('S')
    else:
        print('N')
    return 1
        
"""    
    for i in range (0,n-2,2):
        while lista[i+1]>lista[i] and lista[i+1]<lista[i+2):
            b = lista[i+1]
            j = i+2
        
            b
        
"""

n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
lista = []

for i in range(0,n,1):
    lista.append(int(input('digite valor: ')))

pico(lista)

