# -*- coding: utf-8 -*-
import math
a=int(input('Digite o Valor do M:'))
soma=0
x = 2
y = 3
z = 4
for i in range(1,a+1,1):
    if i%2==1:
      soma=soma+4/(x*y*z)
    else: 
      soma=soma-4/(x*y*z)
    x=x+2
    y=y+2
    z=z+2
sgeral=soma+3
  
print('%.6f' %soma)