# -*- coding: utf-8 -*-
import math


def mdc(a,b):
    for i in range (a,0,-1):
        if b%i==0:
            print (i)

n=int(input("Digite o primeiro número:"))
m=int(input("Digite o segundo número:"))

if n>=m:
    mdc(n,m)
else:
    mdc(m,n)
    



