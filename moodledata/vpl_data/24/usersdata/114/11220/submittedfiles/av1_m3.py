# -*- coding: utf-8 -*-
from __future__ import division
import math

m=int(input('valor de m: '))

soma=3
a=2
b=3
c=4
i=2
while i<=m:
      if (i%2)==0:
          soma=soma + (4 / (a*b*c))
      else:
          soma=soma - (4 / (a*b*c))
      a=a + 2
      b=b + 2
      c=c + 2
      i=i + 1
print ('o valor de pi é igual a %.6f' %soma)      