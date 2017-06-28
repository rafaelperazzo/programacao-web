# -*- coding: utf-8 -*-
def degraus(lista):
    b=[]
    for i in range(0,(len(lista)-1),1):
        f=abs(lista[i]-lista[i+1])
        b.append(f)
        cont=0
        for i in range(0,len(b),1):
            if b[i]>cont:
                cont=b[i]
    return cont
n=int(input('digite a quantidade de termos das listas:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite o numero:'))
    a.append(numero)
print(degraus(a))    