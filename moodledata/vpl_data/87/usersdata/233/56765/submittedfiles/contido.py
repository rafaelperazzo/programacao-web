# -*- coding: utf-8 -*-
def interseção(listaa,listab):
    cont=-9
    if len(listaa)<len(listab):
        for i in range(0,len(listaa),1):
            for j in range(0,len(listab)):
                if listaa[i]==listab[j]:
                    cont=cont+1
    else:
        if len(listab)<len(listaa):
            for i in range(0,len(listab)):
                for j in range(0,len(listaa)):
                    if listab[i]==listaa[j]:
                        cont=cont+1
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
