# -*- coding: utf-8 -*-
n=int(input('n:'))
m=int(input('m:'))
a=[]
b=[]
for i in range (0,n,1):
    num=float(input('digite o numero:'))
    a.append (num)
for i in range (0,m,1):
    num=float(input('digite o numero:'))
    b.append (num)
def iguais(a,b):
    cont=0    
    for i in range (0,n,1):
        for j in range (0,m,1):
            if a[i]==b[j]:
                cont=cont+1
    return cont
    
            
            
           


