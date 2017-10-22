# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento= float(input('Digite seu investimento:'))
taxa= float(input('Digite sua taxa de crescimento anual:'))
while (true):
    investimento=investimento*taxa
    print ('% .2F'  %investimento)
