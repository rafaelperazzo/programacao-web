# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

na=c//a
nb=(c%a)//b

if (na*a+nb*b)==c:
    print na
    print nb

nb=c//b
na=(c%b)//a

elif (nb*b+na*a)==c:
    print na
    print nb

else:
    print ('Não')