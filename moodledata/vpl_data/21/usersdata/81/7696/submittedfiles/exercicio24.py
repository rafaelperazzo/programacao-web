# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=ont(input('Digite o valor de B:'))
mdc=1
i=2
while i<=a:
    if a%i==0 and b%i==0:
        mdc=i
        print(mdc)