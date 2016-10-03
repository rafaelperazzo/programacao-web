# -*- coding: utf-8 -*-
from __future__ import division
import math
a= input(' digite o salário:')
if 1000<a<=3000:
    y=(a-1000)
    imp= (y*0.2)
    print(imp)
if a>3000:
    x=(a-3000)
    imp=(x*0.35) + (y*0.2)
    print(imp)
if a<=1000:
    imp=0
    print(imp)