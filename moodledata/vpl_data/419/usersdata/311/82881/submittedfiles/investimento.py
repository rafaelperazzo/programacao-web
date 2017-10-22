# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento= float(input('Digite seu investimento:'))
taxa= float(input('Digite sua taxa de crescimento anual:'))
i=1
while (i<10):
    i+=1
    investimento=investimento + investimento*taxa
    print ('%.2F'  %investimento)
    break