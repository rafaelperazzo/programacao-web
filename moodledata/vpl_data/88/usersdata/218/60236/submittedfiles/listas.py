# -*- coding: utf-8 -*-
def degraus(lista):
    for i in range(0,(len(lista)-1),1):
        D=0
        f=abs(lista[i]-lista[i+1])
        if f>D:
            D=f
    return D
n=int(input('digite a quantidade de termos das listas:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite o numero:'))
    a.append(numero)
print(degraus(a))    