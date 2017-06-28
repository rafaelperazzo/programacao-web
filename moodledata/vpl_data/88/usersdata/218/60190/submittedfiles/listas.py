# -*- coding: utf-8 -*-
def degraus(lista):
    for i in range(0,len(lista),1):
        degrau=0
        if abs((lista[i]-lista[i+1]))>degrau:
            degrau=abs(lista[i]-lista[i+1])
    return degrau
n=int(input('digite a quantidade de termos das listas:'))
a=[]
for i in range (0,n,1):
    numero=float(input('digite o numero:'))
    a.append(numero)
print(degraus(a))    