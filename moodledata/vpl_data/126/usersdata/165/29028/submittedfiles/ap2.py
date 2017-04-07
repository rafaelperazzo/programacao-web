# -*- coding: utf-8 -*-
a=float(input('digite um valor para a:'))
b=float(input('digite um valor para b:'))
c=float(input('digite um valor para c:'))
d=float(input('digite um valor para d:'))
if a>=b and a>=c and a>=d:
    print('%.f' %a)
    if b<=c and b<=d:
        print('%.f' %b)
    elif c<=b and c<=d:
        print('%.f' %c)
    else:
        print('%.f' %d)
elif b>=a and b>=c and b>=d:
    print('%.f' %b)
    if a<=c and a<=d:
        print('%.f' %a)
    elif c<=a and c<=d:
        print('%.f' %c)
    else:
        print('%.f' %d)
elif c>=a and c>=b and c>=d:
    print('%.f' %c)
    if a<=b and a<=d:
        print('%.f' %a)
    elif b<=a and b<=d:
        print('%.f' %b)
    else:
        print('%.f' %d)
else:
    print('%.f' %d)
    if a<=b and a<=c:
        print('%.f' %a)
    elif b<=a and b<=c:
        print('%.f' %b)
    else:
        print('%.f' %c)
        