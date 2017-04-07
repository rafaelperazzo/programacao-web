# -*- coding: utf-8 -*-
w=int(input('digite w:'))
x=int(input('digite x:'))
y=int(input('digite y:'))
z=int(input('digite z:'))
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
    elif z<=w and z<=x:
        print(z)
elif z>=w and z>=x and z>=y:
    print(z)
    if w<=x and w<=y:
        print(w)
    elif x<=w and x<=y:
        print(x)
    elif y<=w and y<=x:
        print(y)
    

