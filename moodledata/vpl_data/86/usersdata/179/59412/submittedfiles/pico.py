# -*- coding: utf-8 -*-

def pmax(a):
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            return(i)
def pico(a):
    cont=0
    x=pmax(a)
    for i in range(x,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==(len(a)-x)-1:
        return True
    else:
        return False
n =int(input('Digite a quantidade de elementos da lista: '))
b=[]
for i in range(0,n,1):
    valor=int(input('digite os valores :'))
    b.append(valor)
if pico(b):
    print('S')
else:
    print('N')
