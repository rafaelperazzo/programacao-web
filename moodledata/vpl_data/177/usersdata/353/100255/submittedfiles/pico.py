# -*- coding: utf-8 -*-

a=[]
n = int(input())
for i in range (0,n,1):
    a.append(int(input()))
    


for i in range (0,n-1,1):
    if a[i]<a[i+1]:
            b=0
    if a[i]>a[i+1]:
        b=1
    
    if b==0:
        if a[i]<a[i+1]:
            b=0
        else:
            b=1
    if b==1:
        if a[i]>a[i+1]:
            b=1
        else:
            b=333
            
if b==333:
    print('N')
else:
    ('S')
    

    
