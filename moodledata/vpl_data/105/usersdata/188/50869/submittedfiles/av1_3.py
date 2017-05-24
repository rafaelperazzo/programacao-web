# -*- coding: utf-8 -*-
import math
N1=int(input('Digite o valor do número 1:'))
N2=int(input('Digite o valor do número 2:'))
N3=int(input('Digite o valor do número 3:'))
n=1
N2=0
while n>0:
    if(n%N1)==0 and (n%N2)==0 and (n%N3)==0:
        N2=N2+n
        break
    else:
        n=n+1
        print ('N2')
    