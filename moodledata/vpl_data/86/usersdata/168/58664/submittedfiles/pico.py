# -*- coding: utf-8 -*-

def pmax(a):
    for i in range (0, len(a)-1,1):
        if a[i]>a[i+1]:
            return (i)
def pico(a):
    x=pmax(a)
    for i in range (x,len(a)-1,1):
        if a[i]<a[i+1]:
            return False
    return True
    
b=[]
n =int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n,1):
    valor=int(input('Valor: '))
    b.append(valor)
if pico(b):
    print('S')
else:
    print('N')
    

