# -*- coding: utf-8 -*-
def degraus(lista):
    for i in range(0,(len(lista)-1),1):
        d=0
        f=lista[i]-lista[i+1]
        if f>0:
            if f>d:
                d=f
        elif f<0:
            d=(-1)*f
    return d
n=int(input('digite a quantidade de termos das listas:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite o numero:'))
    a.append(numero)
print(degraus(a))    