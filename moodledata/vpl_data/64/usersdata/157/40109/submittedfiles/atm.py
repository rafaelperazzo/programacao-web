# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Qual o valor?:'))
if valor/20:
    div20=valor/20
    print('%d'%div20)
if valor/10:
    resto20=valor/20
    div10=resto20/10
    print('%d'%div10)
if valor/5:
    resto10=resto20%10
    div5=resto10/5
    print('%d'%div5)
if valor/2:
    resto5=resto10%5
    div2=resto5/2
    print('%d'%div2)
if valor/1:
    resto2=resto5%2
    div1=resto2/1
    print('%d'%div1)
