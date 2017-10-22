# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento= float(input('DIGITE O VALOR DO INVESTIMENTO:')
taxa= float(input('DIGITE O VALOR DA TAXA:')
a=1
while (a<11):
    total= investimento*((1+ taxa)**a)
    print('%.2f' %total)
    a +=1

