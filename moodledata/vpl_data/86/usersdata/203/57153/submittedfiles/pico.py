# -*- coding: utf-8 -*-
def pico(lista):
    for i in range(0,len(lista)-1,1):
        
        
L=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range(1,n+1,1):
    l=int(input('digite elemento: '))
    L.append(l)
if pico(L):
    print('S')
else:
    print('N')
