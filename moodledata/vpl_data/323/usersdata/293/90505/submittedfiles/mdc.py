# -*- coding: utf-8 -*-
import math

n1=int(input("Digite n1: "))
n2=int(input("Digite n2: "))
mdc=1

if n1>n2:
    for i in range(1,n2+1,1):
        if  n1%i==0 and n2%i==0:
            mdc=i*mdc
    print(mdc)        

