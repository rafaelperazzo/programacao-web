# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
s=0

for i in range(1,n+1,1):
    if i%2==0:
        s=s-(i/(i**2))
    else:
        s=s+(i*(i**2))
    i=i+1
print('%.5f'%s)