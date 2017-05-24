# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor a:'))
b = int(input('digite o valor b:'))
c = int(input('digite o valor c:'))
i=1
cont=0
while i>0:
    if i%a==0 and i%b==0 and i%c==0:
        cont = cont + 1
    i=i+1
print(cont)    

