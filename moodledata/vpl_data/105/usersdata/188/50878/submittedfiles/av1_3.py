# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número 1:'))
b=int(input('Digite o valor do número 2:'))
c=int(input('Digite o valor do número 3:'))
n=1
b=0
while n>0:
    if(n%a)==0 and (n%b)==0 and (n%c)==0:
        b=b+n
        break
else:
    n=n+1
    print ('b')
    