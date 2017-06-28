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

