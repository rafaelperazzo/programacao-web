# -*- coding: utf-8 -*-
def interseção(listaa,listab):
    cont=0
    if len(listaa)<len(listab):
        for i in range(0,len(listaa)):
            for j in range(0,len(listab)):
                if listaa[i]==lista[j]:
                    cont=cont+1
    if len(listab)<len(listaa):
        for i in range(0,len(listab)):
            for j in range(0,len(listaa)):
                if listab[i]==listaa[j]:
                    cont=cont+1
    return cont
n=int(input('n: '))
m=int(input('m: '))
listaa=[]
listab=[]
for i in range(n):
    a=float(input('a: ')
    listaa.append(a)
for i in range(m):
    b=float(input('b: ')
    listab.append(b)
c=interseção(listaa,listab)
print(a)
