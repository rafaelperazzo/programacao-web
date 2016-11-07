# -*- coding: utf-8 -*-
from __future__ import division

def resto(numero,divisor):
    return numero%divisor
    
while True:
    n=input("Número: ")
    if n=="break":
        break
    d=input("Divisor: ")
    print resto(n,d)