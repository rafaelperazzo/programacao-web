# -*- coding: utf-8 -*-
n=int(input('digite valor de n :'))
for i in range(2,n,1):
    if n%i==0:
        print(i)
        print('Não primo')
    if n%i==1:
        print(i)
        print('Primo')









