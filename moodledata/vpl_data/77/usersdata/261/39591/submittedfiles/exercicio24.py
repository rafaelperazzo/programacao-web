# -*- coding: utf-8 -*-
from __future__ import division
import math

def calcmdc(ma,me):    
    while ma%me>0:
        re= ma%me
        ma = ma
        me = re
    print (me)

def mdc():
    a = int(input("Digite o seu 1º número para cálculo: "))
    b = int(input("Digite o seu 2º número para cálculo: "))
    if a>b:
        ma=a
        me=b
        calcmdc(ma,me)
    elif a<b:
        ma=b
        me=a
        calcmdc(ma,me)
    else:
        print ("1")
     
mdc()

