# -*- coding: utf-8 -*-
i= 2
c= 0
n= int(input('digite o valor de n: '))
while(i<n):
    if (n%i)==0:
        c=c+1
    print(i)
i=i+1
if i==0:
    print(' primo')
if i>0:
    print('NÃO PRIMO'))