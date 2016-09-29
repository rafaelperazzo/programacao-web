# -*- coding: utf-8 -*-

from __future__ import division

n= input( )

vinte= (n//20)
dez= (n%20)//10
cinco= ((n%20)%10)//5
dois= (((n%20)%10)%5)//2
um= (((n%20)%10)%5)%2

print(vinte)
print(dez)
print(cinco)
print(dois)
print(um)