# -*- coding: utf-8 -*-
import math


n1 = int(input( 'informe o numero 1: ' ))
n2 = int(input(' informe o numero 2: '))

if n1%9 == 0 and n2%9 == 0:
    print (9)
elif n1%8 == 0 and n2%8 == 0:
    print (8)
elif n1%7 == 0 and n2%7 == 0:
    print (7)
elif n1%6 == 0 and n2%6 == 0:
    print (6)
elif n1%5 == 0 and n2%5 == 0:
    print (5)
elif n1%4 == 0 and n2%4 == 0:
    print (4)
elif n1%3 == 0 and n2%3 == 0:
    print (3)
elif n1%2 == 0 and n2%2 == 0:
    print (2)
else:
    print (1)