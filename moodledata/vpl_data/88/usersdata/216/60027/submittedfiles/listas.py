# -*- coding: utf-8 -*-

def diferenca(a):
    l=[]
    for i in range(0,len(a)-1,1):
        menos=a[i]-a[i+1]
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
        else:
            l.append(menos)
    return(l)

def maior(b):
    for i in range(0,len(b),1):
        c=b[0]
        ma=0
        if (c>=b[i]):
            ma=b[i]
    return(c)

a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)
    
f=diferenca(a)

print(maior(f))