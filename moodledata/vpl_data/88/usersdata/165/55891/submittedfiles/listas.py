# -*- coding: utf-8 -*-
def degrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        x=abs(a[i]-a[i+1])
        if x>maior:
            maior=x
        
    return(maior)
    
n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
print(degrau(a))    

