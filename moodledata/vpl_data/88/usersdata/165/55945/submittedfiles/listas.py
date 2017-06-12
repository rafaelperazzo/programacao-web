# -*- coding: utf-8 -*-
def degrau(a):
    b=[]
    for i in range(0,len(a)-1,1):
        x=abs(a[i]-a[i+1])
        x.append(b)
    return(b)
    
def maior(degrau(a)):
    maior=b[0]
    for i in range(0,len(b),1):
        if b[i]>maior:
            maior=b[i]
    return(maior)        
n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
print(maior(a))    
    

