# -*- coding: utf-8 -*-

def pico(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]<a[i+2]:
            cont=cont+1
            return(True)
        else:
            return(False)
n=int(input('Digite a quantidade de elementos da lista: '))
x=[]
for i in range(0,n,1):
    valor=int(input('digite os elementos:'))
    x.append(valor)
if pico(x)==(True):
    print('S')
else:
    print('N')
