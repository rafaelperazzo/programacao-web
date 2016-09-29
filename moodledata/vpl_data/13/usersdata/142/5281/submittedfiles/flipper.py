# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
X= input('Digite dois números que sejam 1 ou 0:')

P=X//10
R=X%10

if P==1 and R==1:
    print ('A')
elif P==1 and R==0:
    print ('B')
elif P==0 and R==0:
    print ('C')

