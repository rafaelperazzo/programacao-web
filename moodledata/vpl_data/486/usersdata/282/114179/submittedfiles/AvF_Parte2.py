#  -*- coding: utf-8 -*-

while (True):
    id = int(input('Digite sua idade: '))
    h = float(input('Digite sua altura: '))
    if id>18 and h>0:
        print(id)
        print(h)
    elif id<18:
        id = int(input('Digite sua idade: '))
        print(id)
        print(h)
    elif h<0:
        h = float(input('Digite sua altura: '))
        print(id)
        print(h)
        if i==-1:
            break


