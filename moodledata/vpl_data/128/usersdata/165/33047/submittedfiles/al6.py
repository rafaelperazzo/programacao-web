# -*- coding: utf-8 -*-
n=int(input('digite um n:'))
for i in range (2,n,1):
    if n%i==0:
        print(i)
    else:
        print('primo')