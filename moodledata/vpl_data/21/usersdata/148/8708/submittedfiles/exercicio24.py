# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a = input('Digite o primeiro valor :')
b = input('Digite o segundo valor :')
mdc = 1
d = 2
#PROCESSAMENTO
while d<=a :
    if a%d==0 and b%d==0 :
        mdc=d
    d=d+1
print mdc 
        
