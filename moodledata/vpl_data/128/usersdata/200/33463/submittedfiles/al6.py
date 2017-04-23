# -*- coding: utf-8 -*-
n=int(input('digite o numero:'))
d=2
i=0
while d<n:
    if n%d==0:
        print(d)
        i=i+1
    d=d+1
if i==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')