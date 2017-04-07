# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if c<=a and c<=b:
    print ('%d' %a)
    if b<=a:
        print ('%d' %b)
        print ('%d' %a)
    else:
        print ('%d' %a)
        print ('%d' %b)
elif b<=a and b<=c:
    print ('%d' %b)
    if b<=c:
        print ('%d' %a)
        print ('%d' %c)
    else:
        print ('%d' %c)
        print ('%d' %a)
else:
    print ('%d' %a)
    if b<=c:
        print ('%d' %b)
        print ('%d' %c)
    else:
        print ('%d' %c)
        print ('%d' %b)