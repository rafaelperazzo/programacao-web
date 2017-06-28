# -*- coding: utf-8 -*-

def iguais(c,d):
    iguais=0
    for i in range(0,len(d),1):
        for j in range(0,len(c),1):
            if (d[i]==c[j]):
                iguais=iguais+1
    return (iguais)
n=int(input('n:'))
m=int(input('m:'))
a=[]
b=[]
for z in range(0,n,1):
    valorA=int(input('A:'))
    a.append(valorS)
for w in range(0,m,1):
    valorB=int(input('B:'))
    b.append(valorB)
    
print(iguais(a,b)))
