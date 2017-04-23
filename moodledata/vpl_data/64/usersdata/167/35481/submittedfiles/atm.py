# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite n:'))
vinte=(n-n%20)/20
if vinte>0:
    n=n%20
    print('vinte é %f'%vinte)
dez=(n-n%10)/10
if dez>0:
    n=n%10
    print('dez é %f'%dez) 
cinco=(n-n%5)/5
if cinco>0:
    n=n%5
    print('cinco é %f'%cinco)


