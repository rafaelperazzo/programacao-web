# -*- coding: utf-8 -*-

def degrau(b):
    degrau=0
    f=0
    for i in range(0,len(b)-1,1):
        f=b[i]-b[i+1]
        if f<0:
            f=f*(-1)
        if f>degrau:
            degrau=f
    return(degrau)

n=int(input('digite a quantidade de termos:'))
x=[]
for i in range(0,n,1):
    v=int(input('digite o elemento do índice +'i'+ :'))
    x.append(v)
print(degrau(x))