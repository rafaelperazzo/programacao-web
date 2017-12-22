# -*- coding: utf-8 -*-
import math
#
#########    print(mdc)
n = int(input("Digite o valor de n (n > 0): "))
m = int(input("Digite o valor de m (m > 0): "))
mdc = n
    while n % mdc != 0 or m % mdc != 0: 
        mdc = mdc - 1
print("MDC(%d,%d)=%d" %(n,m,mdc))