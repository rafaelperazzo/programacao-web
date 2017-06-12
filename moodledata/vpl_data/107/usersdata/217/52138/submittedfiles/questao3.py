# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
a=0
b=0
for i in range(2,p,1):
    if p%i==0:
        print('N')
        break
    else:
        a=a+1
for i in range(2,q,1):
    if q%i==0:
        print('N')
        break
    else:
        b=b+1
if a==1 and b==1 and q==p+2:
    print('S')
    

    

    
    
    