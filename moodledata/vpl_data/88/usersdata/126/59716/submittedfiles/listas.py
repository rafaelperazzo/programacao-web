# -*- coding: utf-8 -*-


def modulo(a):
    p=[]
    q=[]
    for i in range(0,len(a)-1,1):
        cont=0
        if a[i]>a[i+1]:
            while a[i]>a[i+1]:
                a[i]=a[i]-1
                cont=cont+1
        elif a[i]<a[i+1]:
            while a[i]<a[i+1]:
                a[i]=a[i]+1
                cont=cont+1
        elif a[i]==a[i+1]:
            cont=0
        p.append(cont)
    for i in range(0,len(p)-1,1):
        if p[i]>p[i+1]:
            q.append(p[i])
        elif p[i]<p[i+1]:
            q.append(p[i+1])
        elif p[i]==p[i+!]:
            q.append(p[i])
        
    return(q)
        
        
        
n=int(input('digite o numero de elementos da lista:'))
r=[]
for i in range(0,n,1):
    m=int(input('digite um valor:'))
    r.append(m)


print (modulo(r))