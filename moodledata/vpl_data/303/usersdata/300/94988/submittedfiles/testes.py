# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = 5
a = [1,2,3,4,5]
for i in range(0,n,1):
    p = 0
        if a[i] > a[i-1]:
            p = p+1
    if p == n:
        print('1')
    else:
        print('2')