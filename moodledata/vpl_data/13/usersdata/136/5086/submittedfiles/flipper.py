# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
P = input("Digite o valor da porta P:")
R = input("Digite o valor da porta R:")

if P==0:
    print("C")
if P==1 and R==0:
    print("B")
if P==1 and R==1:
    print("A")