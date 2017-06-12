# -*- coding: utf-8 -*-
def maiordegrau(lista):
    listadegraus=[]
    for i in range(1,len(lista)):
        degrau=lista[i]-lista[i-1]
        if degrau>0:
            degrau=degrau
        else:
            degrau=degrau*(-1)
        listadegraus.append(degrau)
    return(max(listadegraus))
n=int(input('n:'))
lista=[]
for i in range(n):
    a=float(input('a:'))
    lista.append(a)
print('%.d'%maiordegrau(lista))

