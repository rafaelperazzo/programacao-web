# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite n:'))
vinte=(n-n%20)/20
if vinte>0:
    n=n%20
    print('%d'%vinte)

