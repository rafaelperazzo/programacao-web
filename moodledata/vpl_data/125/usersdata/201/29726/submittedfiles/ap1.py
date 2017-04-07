# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if a<=b and a<=c:
    print ('%d' %a)
    if b<=c:
        print ('%d' %b)
        print ('%d' %c)
    else:
        print ('%d' %c)
        print ('%d' %b)
elif b<=a and b<=c:
    print ('%d' %b)
    if a<=c:
        print ('%d' %a)
        print ('%d' %c)
    else:
        print ('%d' %c)
        print ('%d' %a)
else:
    print ('%d' %c)
    if a<=b:
        print ('%d' %a)
        print ('%d' %b)