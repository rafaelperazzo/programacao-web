# -*- coding: utf-8 -*-
n=int(('digite um número:'))
d=2
i=0
while d<n:
    if (n%d)==0:
        print(d)
        d=d+1
        i=i+1
if i==0:
    print('primo')
else:
    else('não primo')