# -*- coding: utf-8 -*-
import math

n1=int(input("Digite n1: "))
n2=int(input("Digite n2: "))
mdc=1
while(True):
    if n1%mdc==0 and n2%mdc==0:
        mdc=mdc-mdc
        print(mdc)
    else:
        mdc=mdc+1
    