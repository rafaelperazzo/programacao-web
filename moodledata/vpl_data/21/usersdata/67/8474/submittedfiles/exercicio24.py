# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input("Digite o primeiro numero:")
b=input("Digite o segundo numero:")
i=a
while a%i!=0 or b%i!=0:
    i=i-1
print(i)

