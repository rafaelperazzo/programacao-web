# -*- coding: utf-8 -*-
import math
n=int(input('n'))
i=1
d=1
soma=0
while i<=n:
    if n%2==0:
        soma=soma-1/(d)
    else:
        soma=+1/(d)
    i=i+1
    d=d+1
print('%.5f'%soma)

