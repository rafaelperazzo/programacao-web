# -*- coding: utf-8 -*-
def interseção(listaa,listab):
    cont=0
    indice=0
    if len(listaa)<len(listab):
        while indice<len(listaa):
            for j in range(0,len(lista(b),1)):
                if listaa[indice]==listab[j]:
                    cont=cont+1
            indice=indice+1
    else:
        while indice<len(listab):
            for j in range(0,len(lista(a),1)):
                if listab[indice]==listaa[j]:
                    cont=cont+1
            indice=indice+1
    return cont
n=int(input('n: '))
m=int(input('m: '))
lista1=[]
lista2=[]
for i in range(n):
    a=float(input('a: '))
    lista1=lista1+[a]
for i in range(m):
    b=float(input('b: '))
    lista2=lista2+[b]
c=interseção(lista1,lista2)
print(a)
