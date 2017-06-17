# -*- coding: utf-8 -*-

def cres(lista):
    for j in range (0, len(lista)-1, 1):
        if (lista[j]>lista[j+1]):
            return(False)
    return(True)
    
def decres(lista):
    for j in range (0, len(lista)-1, 1):
        if (lista[j]<lista[j+1]):
            return(False)
    return(True)    

n=int(input('Digite a quantidade de elementos das listas: '))
a=[]
b=[]
c=[]
for i in range (1, n+1, 1):
    valor=int(input('Digite os elementos da lista: '))
    a.append(valor)
for i in range (1, n+1, 1):
    valor=int(input('Digite os elementos da lista: '))
    b.append(valor)
for i in range (1, n+1, 1):
    valor=int(input('Digite os elementos da lista: '))
    c.append(valor)
if (cresc(a)):
    print('S')
else:
    print('N')
if (decresc(a)):
    print('S')
else:
    print('N')
if (cresc(b)):
    print('S')
else:
    print('N')
if (decresc(b)):
    print('S')
else:
    print('N')
if (cresc(c)):
    print('S')
else:
    print('N')
if (decresc(c)):
    print('S')
else:
    print('N')    