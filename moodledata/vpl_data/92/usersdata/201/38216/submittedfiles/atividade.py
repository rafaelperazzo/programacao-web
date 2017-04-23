# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
soma=0
num=1
den=n
for i in range(1,n+1,1):
    soma=soma+(num/den)
    num=num+1
    den=n-i
print('%.5f' %soma)
if n<0:
    n*(-1)
for i in range(1,n+1,1):
      soma=soma+(num/den)
      num=num+1
      den=n-i
print('%.5f' %soma) 

