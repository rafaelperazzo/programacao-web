# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista) :
    cont=0
    for i in range (0,len(lista),1):
        if i==0 :
            if lista[i]>lista[i+1] and lista[i]>lista[i-1] :
            cont=cont+1
        elif i=len(i)-1 :
            if lista[i]>lista[i+1] and lista[i]>lista[i-1] :
            cont=cont+1
        else :
            cont=cont+1
    if cont==1 :
        return True
    else :
        return False

la = []
lb = []

a = input('Digite o tamanho da lista: ')

for i in range (0,a,1):
    la.append(input('Digite o valor do elemento: '))

for i in range (0,a,1):
    lb.append(input('Digite o valor do elemento: '))

leckerLa=lecker(la)
leckerLb=lecker(lb)

if lecker(la) :
    print ('S')
else :
    print ('N')

if lecker(lb) :
    print ('S')
else :
    print ('N')