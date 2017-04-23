# -*- coding: utf-8 -*-
import math

x1 = int(input('Digite x1: '))
x2 = int(input('Digite x2: '))
x3 = int(input('Digite x3: '))
x4 = int(input('Digite x4: '))
x5 = int(input('Digite x5: '))
x6 = int(input('Digite x6: '))
x7 = int(input('Digite x7: '))
x8 = int(input('Digite x8: '))
x9 = int(input('Digite x9: '))

#CONTINUE...
if x1==x2==x3 and x1==x4==x7 and x1==x5==x9 and x3==x5==x7 and x3==x6==x9 and x7==x8==x9 and x4==x5==x6 and x7==x8==x9 and x2==x5==x8:
    if x1==x2==x3 and x1==x4==x7 and x1==x5==x9 and x3==x5==x7 and x3==x6==x9 and x7==x8==x9 and x4==x5==x6 and x7==x8==x9 and x2==x5==x8 == 1:
        print('jogador 1 venceu')
    else:
        print('jogador 0 venceu')
else:
    print('empate')

