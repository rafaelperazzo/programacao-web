# -*- coding: utf-8 -*-
import math
m=(int(input('Digite o valor: '))
c=4
cont=0
a=0
b=2
for i in range (0,m,1):
    a=4/(b*(b+1)*(b+2))
    cont=cont+1
    if (cont%2 ==0):
        c=c-a
    if (cont%2==1):
        c=c+a
print('%.6'%a)