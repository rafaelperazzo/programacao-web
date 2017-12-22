# -*- coding: utf-8 -*-
import math
n1=int(input('N1:'))
while n1<=0:
    n1=int(input('N1:'))
n2=int(input('N2:'))
while n2<=0:
    n2=int(input('N2:'))
if n1>n2:
    if n1%n2==0:
        mdc=(n2)
    print(mdc)
    #else :
        #while (n2%(n1%n2)==0):
#print(mdc) 
