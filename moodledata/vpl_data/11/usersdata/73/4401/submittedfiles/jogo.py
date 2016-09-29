# -*- coding: utf-8 -*-
from __future__ import division
import math

cv = input ('digite cv:')
ce = input ('digite ce:')
cs = input ('digite cs:')
fv = input ('digite fv:')
fe = input ('digite fe:')
fs = input ('digite fs:')

if ((3*cv)+ce)>((3*fv)+fe):
    print ('C')
if ((3*cv)+ce)<((3*fv)+fe):
    print ('F')
if ((3*cv)+ce)==((3*fv)+fe):
    if cs>fs:
        print ('C')
    if fs>cs:
        print ('F')
    if cs==fs:
        print ('=')
        