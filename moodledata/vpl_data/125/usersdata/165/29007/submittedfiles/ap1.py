# -*- coding: utf-8 -*-
a=float(input('digite um valor para a:'))
b=float(input('digite um valor para b:'))
c=float(input('digite um valor para c:'))
if a<=b and a<=c:
    print('%.f' %a)
    if b<=c:
        print('%.f' %b)
        print('%.f' %c)
    else:
        print('%.f' %c)
        print('%.f' %b)
elif b<=a and b<=c:
    print('%.f' %b)
    if a<=c:
        print('%.f' %a)
        print('%.f' %c)
    else:
        print('%.f' %c)
        print('%.f' %a)
else:
    print('%.f' %c)
    if a<=b:
        print('%.f' %a)
        print('%.f' %b)
    else:
        print('%.f' %b)
        print('%.f' %a)
            
            