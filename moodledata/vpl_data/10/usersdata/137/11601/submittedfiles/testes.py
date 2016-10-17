# -*- coding: utf-8 -*-
from __future__ import division
import math


mv=0
for i in range (0,5,1):
    venda=int(input('digite a venda:'))
    if venda>= mv:
        mv=venda
    print mv
    