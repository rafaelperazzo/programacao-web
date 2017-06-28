# -*- coding: utf-8 -*-
def degraus(lista):
    for i in range(0,(len(lista)-1),1):
        cont=0
        f=abs(lista[i]-lista[i+1])
        print(f)
        if f>cont:
            cont=f
    return cont
n=int(input('digite a quantidade de termos das listas:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite o numero:'))
    a.append(numero)
print(degraus(a))    