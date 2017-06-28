# -*- coding: utf-8 -*-

def degrau(a):
    
    for i in range(0,len(a)-1,1):
        if a[i]>=0 and a[i+1]>=0 and a[i]>=a[i+1]:
            c=a[i]-a[i+1]
            s.append(c)
        elif a[i]>=0 and a[i+1]>=0 and a[i]<=a[i+1]:
            c=a[i+1]-a[i]
            s.append(c)
        elif a[i]>=0 and a[i+1]<0:
            c=a[i]+a[i+1]
            s.append(c)
        elif a[i]<0 and a[i+1]>=0:
            c=a[i]+a[i+1]
            s.append(c)
def maior(w):
    for i in range(0,len(w)-1,1):
        
            
            
        
        
    
        
s=[]
b=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    valor=int(input('digite valor:'))
    b.append(valor)
print(degrau(b))
print(s)


    
    


    
    

