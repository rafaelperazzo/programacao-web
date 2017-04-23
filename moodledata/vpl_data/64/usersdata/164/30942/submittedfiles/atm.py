# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor= int(input('Digite o valor desejado: '))
if (valor/20):
    div20= valor/20
    print('%d' %div20)
else:
    if (valor/10):
        resto20= valor%20
        div10= resto/10
        print('%d' %div10)
    else:
        if (valor/5):
            resto10= valor%10
            div5= resto/5
            print('%d' %div5)
        else:
            if (valor/2):
                resto5= valor%5
                div2= resto/2
                print('%d' %div2)
            else:
                resto2= valor%2
                div1= resto/1
                print('%d' %div1)
