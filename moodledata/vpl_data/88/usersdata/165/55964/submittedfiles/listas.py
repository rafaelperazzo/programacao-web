# -*- coding: utf-8 -*-
def degrau(a):
    b=[]
    for i in range(0,len(a)-1,1):
        x=abs(a[i]-a[i+1])
        b.append(x)
    return(b)
    
def maior(a):
    c=degrau(a)
    maior=c[0]
    for i in range(0,len(c),1):
        if c[i]>maior:
            maior=c[i]
    
    return(maior)        

n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
print(maior(a))    
    

