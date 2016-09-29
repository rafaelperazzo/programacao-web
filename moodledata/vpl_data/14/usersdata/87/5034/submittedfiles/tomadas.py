# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

T1 = input(" numero de tomadas primeiro:")
T2 = input(" numero de tomadas segundo:")
T3 = input(" numero de tomadas terceiro:")
T4 = input(" numero de tomadas quarto:")

T=T1-1
P=T2-1+T
F=T3-1+P
G=T4+F

print("tomadas: %.1f" %G)
