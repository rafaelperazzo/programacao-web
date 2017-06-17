# -*- coding: utf-8 -*-
a=[]
n=int(input('digite a quantidade de termos:'))
for i in range(0,n,1):
    x=int(input('digite os termos:'))
    a.append(x)
b=[]
for i in range(0,len(a)-1,1):
    if a[i]>0 and a[i+1]>0:
        
        if a[i]>a[i+1]:
            degrau=a[i]-a[i+1]
            b.append(degrau)
        if a[i]==a[i+1]:
            degrau==a[i]-a[i+1]
            b.append(degrau)
        if a[i]<a[i+1]:
            degrau=a[i+1]-a[i]
            b.append(degrau)
            
    elif a[i]<0 and a[i+1]>0:
        degrau=(a[i]*(-1))+a[i+1]
        b.append(degrau)
        
    elif a[i]>0 and a[i+1]<0:
        degrau=a[i]+(a[i+1]*(-1))
        b.append(degrau)
        
    elif a[i]==0 and a[i+1]>0:
        degrau=a[i]+a[i+1]
        b.append(degrau)
        
    elif a[i]==0 and a[i+1]<0:
        degrau=a[i]+(a[i+1]*(-1))
        b.append(degrau)

    elif a[i]<0 and a[i+1]<0:
        if a[i]<a[i+1]:
            degrau=(a[i]*(-1))-(a[i+1]*(-1))
            b.append(degrau)
        if a[i]==a[i+1]:
            degrau==0
            b.append(degrau)
        if a[i]>a[i+1]:
            degrau=(a[i+1]*(-1))-(a[i]*(-1))
            b.append(degrau)
maior=b[0]
for i in range(0,len(b),1):
    
    if b[i]>b[i+1]:
        maior=b[i]
print(maior)
    
        
        
        
        