# -*- coding: utf-8 -*-
from __future__ import division

p=('Digite o peso em kilogramas:')
a=('Digite a altura em metros:')
imc=p/(a**2)

if imc<20:
    print'Abaixo'
if imc>=20 and imc<=25:
    print'Normal'
if imc>25 and <=30:
    print'Sobrepeso'
if imc>30 and imc<=40:
    print'Obeso'
if imc>40:
    print'Obesidade'