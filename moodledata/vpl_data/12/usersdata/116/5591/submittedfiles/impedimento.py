# -*- coding: utf-8 -*-
from __future__ import division
import math
L = input ('insira a posição de L:')
R = input ('insira a posição de R:') 
D = input ('insira a posição de D:') 

if R>50 and L<R and R>D: 
    print ('Impedimento')
else: 
    print ('Não há impedimento')