# -*- coding: utf-8 -*-

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if (i==0):
            if (lista[i]>lista[i+1]):
                cont=cont+1
        elif (i==(len(lista)-1)):
            if (lista[i]>lista[i-1]):
                cont=cont+1
        else:
            if ((lista[i]>lista[i+1]) and (lista[i]>lista[i-1])):
                cont=cont+1
    if (cont==1):
        return True
    else:
        return False

n=int(input('Digite o número de elementos: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(float(input('Digite o valor (lista1): ')))
for j in range(0,n,1):
    b.append(float(input('Digite o valor (lista2): ')))

if (lecker(a)):
    print('S')
if (not lecker(a)):
    print('N')
if (lecker(b)):
    print('S')
if (lecker(b)):
    print('N')



