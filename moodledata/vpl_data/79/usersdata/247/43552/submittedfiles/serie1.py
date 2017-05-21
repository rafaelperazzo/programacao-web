# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
soma=0
for i in range(1,n+1,1):
    x=i/(i*i)
    if t%2==0:
        soma=soma-x
    else:
        soma=soma+x
print('a soma é: %.5f' %soma)
    
    