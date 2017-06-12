# -*- coding: utf-8 -*-

def pico(b):
    cres=0
    decres=0
    for i in range (0, len(b), 1):
        while (b[i]<b[i]+1):
            decres=decres+1
        while (b[i]>b[i]+1):
            cres=cres+1
    cont=decres+cres
    if (len(b)==cont):
        print('S')
    else:
        print('N')
    return(pico)        

n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for z in range (1, n+1, 1):
    valor=float(input('Digite os elementos da lista: '))
    a.append(valor)
print(pico(a))    

