# -*- coding: utf-8 -*-
import math
l=int(input('Digite a posição do lançador:'))
r=int(input('Digite a posição do atacante:'))
d=int(input('Digite a posição do zagueiro:'))
if r>50 and r<d and l<r:
    print('N')
elif r>50 and r>d:
    print('S')