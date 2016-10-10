# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input ('digite a quantidade de divisores desejados: ')
a= int(input('digite o valor de a: '))
b= int(input('digite o valor de b:' ))

multiplo= 1
contador= 0

while contador <n:
    if multiplo %a==0 or multiplo %b==0:
        print (multiplo)
        contador= contador + 1
    multiplo= multiplo+ 1
 
