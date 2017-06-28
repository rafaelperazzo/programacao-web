# -*- coding: utf-8 -*-
def maiorAltura(lista):
    resultado=abs(lista[0]-lista[1])
    for i in range(0,len(lista)-1,1):
        if abs(lista[1]-lista[i+1])>resultado:
            resultado=abs(lista[i]-lista[i+1])
    return (resultado)
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    a.append(valor)
maiorDegrau=maiorAltura(a)
print(maiorDegrau)
