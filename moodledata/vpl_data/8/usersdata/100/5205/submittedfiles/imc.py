# -*- coding: utf-8 -*-
from __future__ import division
a = input ('peso em kg:')
al = input ('altura:')
imc = a /(al*al)
if imc < 20:
    print 'abaixo'
elif 20< imc <=25:
    print 'normal'
elif 25< imc <= 30:
    print 'obeso'
elif 30< imc<= 40:
    print 'obesidade'
else:
    print 'obesidade grave'