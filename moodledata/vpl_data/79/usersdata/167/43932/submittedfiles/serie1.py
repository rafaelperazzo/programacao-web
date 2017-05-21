# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
for i in range(1,n+1,1):
    x=i/(i*1)
    if i%2!=0:
        soma=soma+x
    else:
        soma=soma-x
print('s é %.5f' %soma)

