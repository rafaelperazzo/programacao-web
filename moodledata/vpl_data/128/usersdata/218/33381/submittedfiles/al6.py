# -*- coding: utf-8 -*-
n=int(input('digite n:'))
for i in range (2,n,1):
    if n%i==0:
        print(i)
        F=F+1
 if F<1:
    print('não primo')
else: 
    print('primo')
    