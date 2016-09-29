# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L = input(" Lançador:")
R = input("Recebedor:")
D = input("Defensor:")

if R>50 and L<R and R>D:
    print("S")
else:
    print("N")