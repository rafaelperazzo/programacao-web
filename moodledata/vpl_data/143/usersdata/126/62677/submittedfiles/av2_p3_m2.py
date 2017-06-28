# -*- coding: utf-8 -*-
def listadegraus(a):
    c=[]
    for i in range(0,len(a)-1,1):
       b=abs(a[i]-a[i+1])
       c.insert(0,b)
    return(c)

n=int(input('digite a quantidade de termos da lista:'))
a=[]
for i in range(0,n,1):
    m=int(input('digite um valor:'))
    a.append(m)
print(listadegraus(a))

    