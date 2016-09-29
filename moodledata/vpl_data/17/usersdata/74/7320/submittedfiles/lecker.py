# -*- coding: utf-8 -*-
from __future__ import division
import math

a1 = input('primeiro valor: ')
a2 = input('segundo valor: ')
a3 = input('terceiro valor: ')
a4 = input('quarto valor: ')

if a1>a2 and a3<=a2 and a4<=a3:
    print('S')
elif a2>a1 and a2>=a3 and a3>=a4:
    print('S')
elif a3>a2 and a3>=a4 and a2>=a1:
    print('S')
elif a4>a3 and a3>=a2 and a2>=a1:
    print('S')
else:
    print('N')