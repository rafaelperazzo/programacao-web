# -*- coding: utf-8 -*-

def degrau(a):
    dif=0
    degrau=0
    
    for i in range(0,len(a)-1,1):
        dif=a[i]-a[i+1]
        if dif<0:
            dif=dif*(-1)
        if dif>degrau:
            degrau=dif
    return degrau
       
a=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    valor=int(input('digite valor:'))
    a.append(valor)
print(degrau(a))print(s)


    
    


    
    

