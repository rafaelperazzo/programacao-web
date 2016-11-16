# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    if n%2==0:
        cont1=0
        for i in range(0, (n/2)-1, 1):
            if lista[i]<(lista[i]+1):
                cont=cont+0
            else:
                cont= cont+1
        cont2=0
        for i in range((n/2)+1, n-1, 1):
            if lista[i]>(lista[i]-1):
                cont=cont+0
            else:
                cont= cont+1
        if cont1+cont2==0:
            return True
        else:
            return False
    if n%2!=0:
        cont1=0
        for i in range(0, (n//2), 1):
            if lista[i]<(lista[i]+1):
                cont=cont+0
            else:
                cont= cont+1
        cont2=0
        for i in range((n//2)+1, n-1, 1):
            if lista[i]>(lista[i]-1):
                cont=cont+0
            else:
                cont= cont+1
        if cont1+cont2==0:
            return True
        else:
            return False

n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0, n, 1):
    a.append(input('Digite a: '))

if pico(a):
    print('S')
else:
    print('N')




