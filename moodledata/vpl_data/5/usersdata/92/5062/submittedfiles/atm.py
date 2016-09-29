# -*- coding: utf-8 -*-

from __future__ import division

n= input( )

vinte= int((n//20))
dez= int((n%20)//10)
cinco= int(((n%20)%10)//5)
dois= int((((n%20)%10)%5)//2)
um= int((((n%20)%10)%5)%2)

print(vinte)
print(dez)
print(cinco)
print(dois)
print(um)