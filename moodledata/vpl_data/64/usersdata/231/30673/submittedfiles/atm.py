# -*- coding: utf-8 -*-
from __future__ import division
import math

saque=int(input('digite o valor'))
if saque>0:
    v1=saque/20
    print('int%.1f'%v1)
    elif v1>10 :
        v2=saque/10
        print('%.1f'%v2)
        elif saque>5:
            v3=saque/5
            print('%.1f'%v3)
            elif saque>2:
                v4=saque/2
                print('%.1f'%v4)
                elif saque>1:
                    v5=saque/1
                    print('%.1f'%v5)
                    else:
                        print('erro')
