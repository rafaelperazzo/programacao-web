# -*- coding: utf-8 -*-
x=float(input('digite x:'))
y=float(input('digite y:'))
z=float(input('digite z:'))
w=float(input('digite w:'))
if x>=y and x>=z and x>=w:
    print('%d'%x)
elif y>=x and y>=z and y>=w:
    print('%d'%y)
elif z>=x and z>=y and z>=w:
    print('%d'%z)
else:
    print('%d'%w)
if x<=y and x<=z and x<=w:
    print('%d'%x)
elif y<=x and y<=z and y<=w:
    print('%d'%y)
elif z<=x and z<=y and z<=w:
    print('%d'%z)
else:
    print('%d'%w)