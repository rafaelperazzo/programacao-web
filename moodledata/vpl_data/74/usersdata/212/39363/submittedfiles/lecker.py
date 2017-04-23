# -*- coding: utf-8 -*-
import math
n1=float(input('digite o valor do primeiro número:'))
n2=float(input('digite o valor do segundo número:'))
n3=float(input('digite o valor do terceiro número:'))
n4=float(input('digite o valor do quarto número:'))
if n1>n2 and n2>=n3 and n3>=n4 and n3>=n2 and n4>=n3:
    print('S')
elif n2>n1 and n2>=n3 and n4<=n3:
    print('S')
elif n3>n2 and n3>=n4 and n1<=n2:
    print('S')
elif n4>n3 and n3>=n2 and n2>=n1:
    print('S')
else:
    print('N')
