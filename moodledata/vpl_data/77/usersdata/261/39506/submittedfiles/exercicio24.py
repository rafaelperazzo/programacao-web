# -*- coding: utf-8 -*-
from __future__ import division
import math
def mdc():
    a = int(input("Digite o seu 1º número para cálculo: "))
    b = int(input("Digite o seu 2º número para cálculo: "))
    if a>b:
        ma=a
        me=b
    elif a<b:
        ma=b
        me=a
    else:
        print ("1")
    while ma%me>0:
        re= ma%me
        ma = ma
        me = re
    print me
    
mdc()