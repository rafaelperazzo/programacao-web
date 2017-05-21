# -*- coding: utf-8 -*-
n=int(input('digite um valor'))
s=0
for i in range(1,n,1):
    if(n%i==0):
        print(i)
        s=s+i
if(s==n):
    print('perfeito')
else:
    print('não perfeito')