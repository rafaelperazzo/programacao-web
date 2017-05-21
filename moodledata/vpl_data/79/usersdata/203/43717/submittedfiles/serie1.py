# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
soma=0
for i in range(1,n+1,1):
    var=i/(i*i)
    if i%2!=0:
        soma= soma+var
    else:
        soma= soma-var
print ('%.5f' %soma)