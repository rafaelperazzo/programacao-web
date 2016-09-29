# -*- coding: utf-8 -*-
from __future__ import division

p= input ('digite o peso:')
a= input('digite a altura:')

IMC= (p/(a**2))

if IMC<20:
    print 'abaixo'
if 25<IMC<=30:
    print 'sobrepeso'
if 30<IMC<=40:
    'obesidade'
if IMC>40:
    print 'obesidade grave'
