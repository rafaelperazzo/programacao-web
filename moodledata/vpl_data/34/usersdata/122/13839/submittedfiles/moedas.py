# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor da moeda a:')
b=input('Digite o valor da moeda b:')
c=input('Digite o valor da cedula:')
conta=0
contb=0

while c//a==0:
    conta=conta+1
    a=a+a
    print conta