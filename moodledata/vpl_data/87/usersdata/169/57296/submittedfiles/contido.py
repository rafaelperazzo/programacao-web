# -*- coding: utf-8 -*-
def iguais(e,d):
    iguais=0
    for i in range(0,len(d),1):
        for j in range(0,len(c),1):
            if (d[i]==c[j]):
                iguais=iguais+1
    return(iguais)
n=int(input('Digite a Quantidade de Elementos de L1:'))
m=int(input('Digite a Quantidade de Elementos de L2:'))
l1=[]
l2=[]
for l in range(0,n,1):
    v1=int(input('Digite Elementos da L1:'))
    l1.append(v1)
for m in range(0,n,1):
    v2=int(input('Digite Elementos da L2:'))
    l2.append(v2)
print (iguais(l1,l2))


