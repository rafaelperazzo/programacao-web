# -*- coding: utf-8 -*-
import math
l1=int(input('digite o primeiro valor: '))
l2=int(input('digite o segundo valor: '))
l3=int(input('digite o terceiro valor: '))
l4=int(input('digite o quarto valor: '))
if l1>l2 and l1>l3 and l1>l4:
    print('S')
elif l2>l1 and l2>l3 and l2>l4:
    print('S')
elif l3>l2 and l3>l1 and l3>l4:
    print('S')
elif l4>l2 and l4>l3 and l4>l1:
    print('S')
else:
    print('N')