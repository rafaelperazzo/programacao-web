# -*- coding: utf-8 -*-

n=int(input('ooo'))
i=0
while i*(i+1)*(i+2) <= n:
    i=i+1
if i*(i+1)*(i+2)==n:
    print('S')
else :
    print('N')
