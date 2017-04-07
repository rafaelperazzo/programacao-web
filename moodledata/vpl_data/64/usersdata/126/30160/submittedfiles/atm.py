# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

v= int(input('digite o valor a ser sacado:'))

if v%20==0:
    print (v/20)
else:
    if v%20>0 and ((v%20)>=10 and (v%10)==0):
        print v//20
        print (v%20)//10
    else:
        if v%10>0 and ((v%10)>=5 and (v%5)==0):
            print v//20
            print (v%20)//10
            print (v%10)/5
        

