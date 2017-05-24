# -*- coding: utf-8 -*-
import math
a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
c=int(input('Digite um valor: '))
cont=0
for i in range (0,m,1):
    a=4/(b*(b+1)*(b+2))
    cont=cont+1
    if (cont%2 ==0):
        c=c-a
    if (cont%2==1):
        c=c+a
print('%.6'%a)