# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n: '))
i=2
c=0
while (i<n):
    if (n%i)==0:
        c=c+1
        print(i)
    i=i+1
if c==0:
    print('PRIMO')
if c>0:
    print('NAO PRIMO')