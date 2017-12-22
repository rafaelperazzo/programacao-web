# -*- coding: utf-8 -*-

n = int (input('Digite a quantidade de elementos: '))

a = []
b = []

for i in range (0,n,1):
    valor_b = float (input('Digite o elemento da primeira lista:' ))
    b.append (valor_a)
for i in range (0,n,1):    
    valor_b = float (input('Digite o elemento da segunda lista:' ))
    b.append (valor_b)

def lecker (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if (i == 0):
            if lista[i]>lista[i+1]:
                cont = cont + 1
        elif (i == len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                cont = cont + 1
        else:
            if lista[i]>lista[i+1] and lista [i]>lista[i-1]:
                cont = cont +1
        if cont == 1:
            return (True)
        if cont != 1:
            return (False)
            
if lecker (a):
    print ('S')
    
else:
    print ('N')
    
if lecker (b):
    print ('S')
    
else:
    print ('N')
    