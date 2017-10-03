# -*- coding: utf-8 -*-
import math

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))

i=1
mdc=0

while (i<=a):
    if (a%i==0) and (b%i==0):
        mdc=i
        print(i)
    i=i+1
    