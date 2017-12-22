# -*- coding: utf-8 -*-
import math

x= int(input('Digite um valor: '))
y= int(input('Digite um valor: '))

while (y !=0):
    resto= x%y
    x=y
    y= resto

mdc=x

print(mdc)
