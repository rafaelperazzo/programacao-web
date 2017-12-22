# -*- coding: utf-8 -*-
import math

n1=int(input("Digite n1: "))
n2=int(input("Digite n2: "))
mdc=1

for i in range (2,n1,1):
    if (n1/mdc)%i==0:
        mdc=i*mdc
        print(mdc)