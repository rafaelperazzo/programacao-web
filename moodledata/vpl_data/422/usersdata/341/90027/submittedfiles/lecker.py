# -*- coding: utf-8 -*-
import math

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

if n1 == n2 == n3 == n4:
    print('N')
elif n2>n1 and n2>n3 and n3>=n4:
    print('S')
elif n1>n2 and n3>n4 and n4<=n3:
    print('S')
elif n3>n2 and n3>n4 and n1<=n2:
    print('S')
elif n4>n3>=n2>=n1:
    print('S')
else:
    print('N')
