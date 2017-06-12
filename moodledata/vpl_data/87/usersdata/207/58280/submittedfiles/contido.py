# -*- coding: utf-8 -*-

def iguais(v,l)
    iguai=0
    for i in range(0,len(l),1)
        for c in range(0,len(v),1):
            if (l[i]==v[j]):
                iguais=iguais+1
    return (iguais)
n=int(input('n:'))
m=int(input('m:'))
s=[]
y=[]
for j in range(0,n,1):
    valorS=int(input('S:'))
    s.append(valorS)
for h in range(0,m,1):
    valorY=int(input('Y:'))
    y.append(valorY)
    
print(iguais(s,y))
