# -*- coding: utf-8 -*-
n=int(input('n: '))
lista=[]
degrais=[]
maior=0
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
    a=lista[i]-lista[i+1]
    a=modulo(a)
    degrais.append(a)
for i in range(0,len(degrais),1):
    if degrais[i]>maior:
        maior=degrais[i]
print('%d'%maior)