# -*- coding: utf-8 -*-
def iguais(a,b):
    iguais=0
    for i in range(0,len(b),1):
        for j in range(0,len(a),1):
            if d[i]==c[j]:
                iguais=iguais+1
    return iguais
n=int(input('Quantidade de elementos a: '))
m=int(input('Quantidades de elementos b: '))
a=[]
b=[]
for k in range(1,n+1,1):
    a.append(int(input('Elementos a:'))
for l in range(1,m+1,1):
    b.append(int(input('Elementos b:'))
print iguais(a,b)