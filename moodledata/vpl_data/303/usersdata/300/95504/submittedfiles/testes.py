# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = 5
a = [5,4,3,2,1]
for i in range(1,n,1):
    p = 0
    if (a[i]>a[i-1]):
            p=+1
            print(p)
if p == n:
    print('1')
else:
    print('2')