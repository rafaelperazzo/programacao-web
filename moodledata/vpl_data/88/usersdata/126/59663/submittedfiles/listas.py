# -*- coding: utf-8 -*-


def modulo(a):
    p=[]
    cont=0
    for i in range(0,len(a),1):
        for j in range(a[i],a[i+1],1):
            cont=cont+1
        p.append(cont)
    return(p)
n=int(input('digite o numero de elementos da lista:'))
r=[]
for i in range(0,n,1):
    m=int(input('digite um valor:'))
    r.append(m)

if modulo(r):
    print (p)