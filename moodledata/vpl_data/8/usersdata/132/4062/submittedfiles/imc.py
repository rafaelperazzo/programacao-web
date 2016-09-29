# -*- coding: utf-8 -*-
from __future__ import division
a= input(' digite seu peso em kg:')
b= input(' digite sua altura em metros:')
x=(a/(b**2))
if x<20:
    print('abaixo')
if 20<=x<=25:
    print(' normal')
if 25<x<=30:
    print:('sobre peso')
if 30<x<=40:
    print('obesidade')
if x>40:
    print(' obesidade grave')