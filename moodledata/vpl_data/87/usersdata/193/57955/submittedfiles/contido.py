# -*- coding: utf-8 -*-


def iguais(c,d):
    iguais=0
    for i in range(0,len(d),1):
        for j in range(0,len(c),1):
            if (d[i]==c[j]):
                iguais=iguais+1
    return(iguais)

a=int(input('digite a quantidade de elementos de a:'))
b=int(input('digite a quantidade de elementos de b:'))
c=[]
d=[]
for i in range(0,a,1):
    valora=int(input('digite elemento de a:'))
    c.append(valora)
    
for j in range(0,b,1):
    valorb=int(input('digite elemento de a:'))
    d.append(valorb)
    
print(iguais(c,d))