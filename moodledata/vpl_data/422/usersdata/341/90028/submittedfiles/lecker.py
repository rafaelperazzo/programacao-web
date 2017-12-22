# -*- coding: utf-8 -*-
import math

v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))
v3 = int(input('Digite o terceiro número: '))
v4 = int(input('Digite o quarto número: '))

if v1 == v2 == v3 == v4:
    print('N')
elif v2>v1 and v2>v3 and v3>=v4:
    print('S')
elif v1>v2 and v3>v4 and v4<=v3:
    print('S')
elif v3>v2 and v3>v4 and v1<=v2:
    print('S')
elif v4>v3>=v2>=v1:
    print('S')
else:
    print('N')
