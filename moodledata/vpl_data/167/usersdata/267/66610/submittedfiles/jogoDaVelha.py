# -*- coding: utf-8 -*-
import math
print('Considere as seguintes posições para jogar:')
print('x1|x2|x3')
print('x4|x5|x6')
print('x7|x8|x9')
print()
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

if x1+x2+x3==3 or x4+x5+x6==3 or x7+x8+x9==3 or x1+x4+x7==3 or x2+x5+x8==3 or x3+x6+x9==3 or x1+x5+x9==3 or x3+x5+x7==3:
    print('1')
elif x1+x2+x3==0 or x4+x5+x6==0 or x7+x8+x9==0 or x1+x4+x7==0 or x2+x5+x8==0 or x3+x6+x9==0 or x1+x5+x9==0 or x3+x5+x7==0:
    print('0')
else:
    print('E')
    