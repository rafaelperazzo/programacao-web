# -*- coding: utf-8 -*-
from __future__ import division
p=input(peso em kg)
a=input(altura em metros)
i= p/a**2
if i<20:
    print('ABAIXO')
if 20<=i<=25:
    print('NORMAL')
if 25<i<=30:
    print('SOBREPESO')
if 30<i<=40:
    print('OBESIDADE')
if 40<i:
    print('OBESIDADE GRAVE')
