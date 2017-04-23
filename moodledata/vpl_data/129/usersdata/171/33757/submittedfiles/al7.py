# -*- coding: utf-8 -*-
n=int(input('digite n:'))
c=0
for i in range(1,n,1):
    if n%i==0:
        c=c+i
        print(i)
if c==n:
    print('perfeito')
else:
    print('NAO PERFEITO')