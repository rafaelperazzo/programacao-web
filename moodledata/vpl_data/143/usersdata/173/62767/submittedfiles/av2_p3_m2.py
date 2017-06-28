# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de degraus: '))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('Degrau: '))

b=[]
for i in range(0,n-1,1):
    b.append(a[i]-a[i+1])
for i in range(0,len(b),1):
    if(b[i]<0:
        b[i]=b[i]*(-1)
print(b)