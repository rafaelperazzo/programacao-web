# -*- coding: utf-8 -*-
from __future__ import division

#Definindo a função:
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
        
#Código:
n=input('Digite a quantidade de termos da lista: ')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor para a lista a: '))
    
for i in range(0,n,1):
    b.append(input('Digite um valor para a lista b: '))
if lecker(a):
    print('S')
else:
    print('N')
    
if lecker(b):
    print('S')
else:
    print('N')