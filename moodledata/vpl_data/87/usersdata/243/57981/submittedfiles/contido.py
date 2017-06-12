# -*- coding: utf-8 -*-

def iguais(e,d):
    iguais=0
    for i in range(0,len(e),1):
        if (d[i]==e[j]):
            iguais=iguais+1
    return(iguais)
n=int(input('digite a quantidade de elementos de l1:'))
m=int(input('digite a quantidade de elementos de l2:'))
l1=[]
l2=[]

for i in range (1,n+1,1):
    v1=int(input('digite  os elementos de l1:'))
    l1.append(v1)
for i in range(1,m+1,1):    
    v2=int(input('digite os elementos de l2:'))
    l2.append(v2)
print(iguais(l1,l2))    
