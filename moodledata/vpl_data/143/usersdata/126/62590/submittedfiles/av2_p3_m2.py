# -*- coding: utf-8 -*-
def listadegraus(a):
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=0
            for j in range(a[i],a[i+1]+1,-1):
                cont=cont+1
                b.insert(0,cont)
        elif a[i]<a[i+1]:
            cont=0
            for l in range(a[i],a[i+1]+1,1):
                cont=cont+1
                b.insert(0,cont)
            else:
                cont=0
                b.insert(0,cont)
    return(b)

n=int(input('digite a quantidade de termos da lista:'))
a=[]
for i in range(0,n,1):
    m=int(input('digite um valor:'))
    a.append(m)
print(listadegraus(a))

    