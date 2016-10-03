# -*- coding: utf-8 -*-
from __future__ import division
import math
a= input(' digite o salário:')
y=(a-1000)
if 1000<y<=3000:
    imp= (y*0.2)
    print(imp)
if y>3000:
    imp=y*0.35
    print(imp)
if a<=1000:
    imp=0
    print(imp)