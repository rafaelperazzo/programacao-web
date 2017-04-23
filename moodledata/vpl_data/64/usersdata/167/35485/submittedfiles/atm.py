# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite n:'))
vinte=(n-n%20)/20
if vinte>0:
    n=n%20
    print('vinte é %.1f'%vinte)
dez=(n-n%10)/10
if dez>0:
    n=n%10
    print('dez é %.1f'%dez) 
cinco=(n-n%5)/5
if cinco>0:
    n=n%5
    print('cinco é %.1f'%cinco)
dois=(n-n%2)/2
if dois>0:
    n=n%2
    print('dois é %.1f'%dois)

