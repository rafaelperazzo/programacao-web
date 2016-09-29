# -*- coding: utf-8 -*-
from __future__ import division
import math

L=input('digite a posição do lançador:')
R=('digite a posição do receptor:')
D=('digite a posição do último defensor:')
if R<=50:
    print('N')
elif L>=R:
    print('N')
elif D>=R:
    print('N')
else:
    print('S')

