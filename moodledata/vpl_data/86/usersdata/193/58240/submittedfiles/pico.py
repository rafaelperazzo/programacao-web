# -*- coding: utf-8 -*-

def pico(lista):
    
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]>lista[i+2]:
            
            return(True)
        else:
            return(False)
n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    valor=int(input('digite os elementos:'))
    a.append(valor)
if pico(a)==(True):
    print('S')
else:
    print('N')
