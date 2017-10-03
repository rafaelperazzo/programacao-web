# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a = int(input('Sua aposta: '))
b = int(input('Sua aposta: '))
c = int(input('Sua aposta: '))
d = int(input('Sua aposta: '))
e = int(input('Sua aposta: '))
f = int(input('Sua aposta: '))

g = int(input('Loteria: '))
h = int(input('Loteria: '))
i = int(input('Loteria: '))
j = int(input('Loteria: '))
k = int(input('Loteria: '))
l = int(input('Loteria: '))

if (a == g or a == h or a == i or a == j or a == k or a == l):
    m = 1
elif (b == g or b == h or b == i or b == j or b == k or b == l):
    n = m + 1
elif (c == g or c == h or c == i or c == j or c == k or c == l):
    o = n + 1
elif (d == g or d == h or d == i or d == j or d == k or d == l):
    p = o + 1
elif (e == g or e == h or e == i or e == j or e == k or e == l):
    q = p + 1
elif (f == g or f == h or f == i or f == j or f == k or f == l):
    r = q + 1
    
if r <= 2:
    print('azar')
elif r == 3:
    print('terno')
elif r == 4:
    print('quadra')
elif r == 5:
    print('quina')
elif r == 6:
    print('sena')
    