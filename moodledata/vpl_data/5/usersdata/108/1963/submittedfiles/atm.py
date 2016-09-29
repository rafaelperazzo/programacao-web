# -*- coding: utf-8 -*-
from __future__ import division
import math

v = int(input(' Digite o valor:'))

contador1 = v//20
contador2 = (v%20)//10
contador3 = ((v%20)%10)//5
contador4 = (((v%20)%10)%5)//2
contador5 = (((v%20)%10)%5)%2

print ('%d' %contador1)
print ('%d' %contador2)
print ('%d' %contador3)
print ('%d' %contador4)
print ('%d' %contador5)
    

 
