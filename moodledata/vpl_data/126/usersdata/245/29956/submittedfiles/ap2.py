# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
d=float(input('Digite o valor de d:'))
if a>=b and a>=c and a>=d:
    print('%.1f'%a)
elif b>=a and b>=c and b>=d:
    print('%.1f'%b)
elif c>=a and c>=b and c>=d:
    print('%.1f'%c)
else:
    print('%.1f'%d)
if a<=b and a<=c and a<=d:
    print('%.1f'%a)
elif b<=a and b<=c and b<=d:
    print('%.1f'%b)
elif c<=a and c<=b and c<=d:
    print('%.1f'%c)
else:
    print('%.1f'%d)