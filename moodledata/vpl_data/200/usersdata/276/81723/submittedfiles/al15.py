# -*- coding: utf-8 -*-
n = 1000

while (n<=9999):
    primeiros = n//100
    segundos = n%100
    if ((n)**(1/2) == primeiros + segundos):
        print (n)
    n = n +1