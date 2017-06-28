# -*- coding: utf-8 -*-
n=int(input('n: '))
lista=[]
for i in range(1,n+1,1):
    e=float(input('elemento: '))
    lista.append(e)
def modulo(a):
    if a<0:
        a=a*(-1)
        return a
    else:
        return a
for i in range(0,len(lista)-1,1):
    degrais=[]
    a=lista(i)-lista(i+1)
    a=modulo(a)
    degrais.append(a)
print(degrais)
