# -*- coding: utf-8 -*-
def degrau(y,y):
    for i in range(0,n-1,1):
        y.append(x[i]-x[i+1])
    for i in range(0,len(y),1):
        if (y[i]<0):
            y[i]=y[i]*(-1)
    return (y)
      
    
n=int(input('n:'))
x=[]
y=[]
for i in range(0,n,1):
    valor=int(input('valor'))
    x.append(valor)

print(degrau(x,y))



        
