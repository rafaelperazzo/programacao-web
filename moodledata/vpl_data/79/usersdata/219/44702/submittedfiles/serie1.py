# -*- coding: utf-8 -*-
import math
n=int(input('n'))
i=1
den=1
soma=0
while i<=n:
    if i%2==0:
        soma=soma-1/(den)
    else :
        soma=+1/(den)
    i=i+1
    den=den+1
print('%.5f'%soma)

