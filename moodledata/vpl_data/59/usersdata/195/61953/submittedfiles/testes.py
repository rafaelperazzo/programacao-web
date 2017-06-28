# -*- coding: utf-8 -*-
def maiordegrau(lista):
    listadegrau=[]
    for i in range(1,len(lista)):
        degrau=lista[i]-lista[i-1]
        if degrau>0:
            degrau=degrau
        else:
            degral=(degral)*(-1)
        listadegral.append(degral)
    return(max(listadedegraus))
n=int(input('digite n:'))
lista=[]
for i in range(n):
    a=float(input('digite a:'))
    lista.append(a)
print('%.d'%maiordegrau(lista))
    