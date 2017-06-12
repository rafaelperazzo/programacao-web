# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
c1=0
c2=0
for i in range(2,p-1,1):
    if p%i==0:
        print('N')
        break
    else:
        d1=c1+1
for i in range(2,q-1,1):
    if q%i==0:
        print('N')
        break
    else:
        d2=c2+1
if d1==1 and d2==1 and q==p+2:
    print('S')
    

    

    
    
    