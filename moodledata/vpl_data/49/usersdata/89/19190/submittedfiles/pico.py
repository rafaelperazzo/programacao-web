# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]<lista[1]:
                contador=contador+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                contador=contador+1
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                contador=contador+1
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                contador=contador+1
                
    if contador==len(lista):
        return True
    else: 
        return False
        
#codigo principal
while n<3:
    n=input('digite a quantidade de elementos:')

a=[]

for i in range(0,n,1):
    a.append(input('digite um elemento:'))
    
#chamar a funcao
if pico(a):
    print('S')
else:
    print('N')
    
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
