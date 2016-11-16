# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
def misterio(x):
    cont =0
    for i in range(0,x,1):
        if x%i==0:
            cont = cont +1
            break
        if cont == 0:
            return True
        else:
            return False
y = 100
for i in range(1,y,1):
    if misterio(i):
        print i