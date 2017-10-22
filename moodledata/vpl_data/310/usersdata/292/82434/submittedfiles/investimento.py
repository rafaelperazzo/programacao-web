# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
val=float(input())
perc=float(input())
inv=val*(1+perc)
k=range(1,11)
for i in k:
    print("%.2f"%inv)
    inv=inv*(1+perc)