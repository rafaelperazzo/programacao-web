# -*- coding: utf-8 -*-


def modulo(a):
    p=[]
    cont=0
    for i in range(0,len(a),1):
        for j in range(a[i],a[i+1],1):
            cont=cont+1
        p.append(cont)
    return(cont)
n=int(input('digite o numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    m=int(input('digite um valor:'))
    a.append(m)
    i=i+1
print modulo(a)