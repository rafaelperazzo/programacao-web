# -*- coding: utf-8 -*-

def iguais(c,d):
    iguais=0
    for i in range(0,len(d),1):
        for j in range(0,len(c),1):
            if (d[i]==c[j]:
                iguais=iguais+1
    return(iguais)
    
n=int(input('digite a quantidade de elementos de a:'))
m=int(input('digite a quantidade de elementos de b:'))        
a=[]
b=[]
for i in range(0,n,1):
    valor1=int(input('digite elementos de a:'))
    a.append(valor1)
    
for j in range(0,m,1):
    valor2=int(input('digite elementos de b:'))
    b.append(valor1)

print(iguais(a,b))