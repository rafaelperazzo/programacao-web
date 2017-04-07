# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Difite o valor de c:'))
if a>b or a>c:
   print('%.2f' %a)
elif b>a or b>c:
   print('%.2f' %b)
else:
    print('%.2f' %c)