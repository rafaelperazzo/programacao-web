# -*- coding: utf-8 -*-
import math

n1=int(input("Digite n1: "))
n2=int(input("Digite n2: "))
mdc=1
for i in range (1,n2+1,1):
    if (n1/mdc)%i==0 and (n2/mdc)%i==0:
        mdc=1*i
        print(mdc)
