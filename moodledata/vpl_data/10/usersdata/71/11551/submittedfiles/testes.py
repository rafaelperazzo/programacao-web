# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
i =2

while True:
    if i%a==0 and i%b==0:
        print i
        break
    i=i+1
