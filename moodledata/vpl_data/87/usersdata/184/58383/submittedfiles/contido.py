# -*- coding: utf-8 -*-
def interseção(listaa,listab):
    cont=0
    indice=0
    if len(lista)<len(listab):
        while indice<len(listaa):
            for i in range(0,len(lenlistab),1):
                if listaa[indice]==listab[j]:
                    cont=cont+1
            indice=indice+1
    else:
        while indice<len(listab):
            for j in range(0,len(listaa),1):
                if listab[indice]==listaa[j]:
                    cont=cont+1
            indice=indice+1
    return cont
n=int(input('digite n:'))
m=int(input('digite m:'))
lista1=[]
lista2=[]
for i in range(n):
    a=float(input('a:'))
    lista1=lista1+[a]
for i in range(m):
    b=float(input('b:'))
    lista2=lista2+[b]
c=interseção(lista1,lista2)
print(c)


