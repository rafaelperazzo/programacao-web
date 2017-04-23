# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
i=1
num=1
den=n
termo=0
while i<=n:
    if n>=0:
        termo=termo+(num/den)
        den=den-i
        i=i+1
    if n<0: 
        n*(-1)
        termo=termo+(num/den)
        den=n-1
        i=i+1
        
    
print('%.5f'%termo)


