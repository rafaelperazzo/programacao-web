# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
for i in range(2,p-1,1):
    if p%i==0:
        print('N')
        break
for i in range(2,q-1,1):
    if q%i==0:
        print('N')
        break
else:
    if q==p+2:
        print('S')
        break

    
    
    