# -*- coding: utf-8 -*-
w=float(input('digite w:'))
x=float(input('digite x:'))
y=float(input('digite y:'))
z=float(input('digite z:'))
if w>=x and w<=y and w>=z:
    print(w)
    if x<=y and x<=z:
        print(x)
    elif y<=x and y<=z:
        print(y)
    elif z<=x and z<=y:
        print(z)
elif x>=w and x>=y and x>=z:
    print(x)
    if w<=y and w<=z:
        print(w)
    elif y<=w and y<=z:
        print(y)
    elif z<=w and z<=y:
        print(z)
elif y>=w and y>=x and y>=z:
    print(y)
    if w<=x and w<=z:
        print(w)
    elif x<=w and x<=z:
        print(x)
    elif z<=w and x<=z:
        print(z)
elif z>=w and z>=x and z>=y:
    print(z)
    if w<=x and w<=y:
        print(w)
    elif x<=w and x<=y:
        print(x)
    elif y<=w and y<=x:
        print(y)
    

