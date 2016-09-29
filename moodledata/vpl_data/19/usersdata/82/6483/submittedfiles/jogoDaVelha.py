# -*- coding: utf-8 -*-
from __future__ import division
import math

x1 = input('Digite x1: ')
x2 = input('Digite x2: ')
x3 = input('Digite x3: ')
x4 = input('Digite x4: ')
x5 = input('Digite x5: ')
x6 = input('Digite x6: ')
x7 = input('Digite x7: ')
x8 = input('Digite x8: ')
x9 = input('Digite x9: ')

if (x1==0 and x2==0 and x3==0) or (x4==0 and x5==0 and x6==0) or (x7==0 and x8==0 and x9==0) or (x1==0 and x2==0 and x3==0) or(x1==0 and x5==0 and x9==0) :
    print ('0')
else:
    if (x4==0 and x5==0 and x6==0):
        print ('0')
    else:
        if (x7==0 and x8==0 and x9==0):
            print ('0')
        else:
            if (x1==0 and x2==0 and x3==0):
                print ('0')
            else:
                if (x1==0 and x5==0 and x9==0):
                    print ('0')
                else:
                    if (x3==0 and x5==0 and x7==0):
                        print ('0')
            

