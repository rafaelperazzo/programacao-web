# -*- coding: utf-8 -*-
import math

a=int(input('digite a (a>0): '))
b=int(input('digite b (b>0): '))
#PROCESSAMENTO
mdc=n
while (n%mdc!=0) or (m%mdc!=0):
    mdc=mdc-1
print('mdc(%d,%d)=%d' %(n,m,mdc))