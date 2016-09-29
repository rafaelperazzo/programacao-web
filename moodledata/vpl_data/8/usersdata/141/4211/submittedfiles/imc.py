# -*- coding: utf-8 -*-
from __future__ import division
K=input('informe seu peso K')
A=input('informe seu peso A')
imc=((k)/(A**2))
if imc<20:
    print('abaixo')
if 20<=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')