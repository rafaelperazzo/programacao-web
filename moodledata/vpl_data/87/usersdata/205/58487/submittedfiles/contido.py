# -*- coding: utf-8 -*-
def iguais(e,d):
    iguais=0
    for i in range(0,len(d),1):
        for j in range(0,len(e),1):
           if (d[i]==e[j]):
                 igauis=igauis+1
    return(igauis)
n=int(inpunt('digite a quantidade de elementos de l1:'))
m=int(inpunt('digite a quantidade de elementos de l2:'))
11=[]
12=[]
for l in range(1,n+1,1):
    v1=int(input('digite elementos da l1:'))
    11.append (v1)
for m in range(1,m+1,1):
    v2=int(input('digite elementos da l2:'))
    12.append(v2)
print (iguais(11,12))
        

