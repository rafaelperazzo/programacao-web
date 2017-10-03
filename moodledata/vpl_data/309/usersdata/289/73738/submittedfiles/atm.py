# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE AQUI ABAIXO
valor = int(input("Quanto deseja sacar? ")
if valor<2:
    print("%d" %(valor))
if valor<5 and valor>=2:
    a = valor//2
    print("%d" %(a))
    b = valor%2
    print("%d" %(b))
if valor<10 and valor>=5:
    a = valor//5
    print("%d" %(a))
    b = valor%5
    c = b//2
    print("%d" %(c))
    d = c%2
    print("%d" %(d))
if valor<20 and valor>=10:
    a = valor//10
    print("%d" %(a))
    b = valor%10
    c = b//5
    print("%d" %(c))
    d = b%5
    e = d//2
    print("%d" %(e))
    f = d%2
    print("%d" %(f))
if valor >=20:
    a = valor//20
    print("%d" %(a))
    b = valor%20
    c = b//10
    print("%d" %(c))
    d = b%10
    e = d//5
    print("%d" %(e))
    f = d%5
    g = f//2
    print("%d" %(g))
    h = f%2
    print("%d" %(h))