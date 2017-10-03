# -*- coding: utf-8 -*-
a = int(input('Insira dia 01: '))
b = int(input('Insira mês 01: '))
c = int(input('Insira ano 01: '))
d = int(input('Insira dia 02: '))
e = int(input('Insira mês 02: '))
f = int(input('Insira ano 02: '))
if c > f:
    print('DATA 1')
elif b > e:
    print('DATA 1')
elif a > d:
    print('DATA 1')
elif c == f and b == e and a == d:
    print('IGUAIS')
else:
    print('DATA 2')
    