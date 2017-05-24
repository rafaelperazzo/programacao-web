# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
d1=int(input('digite d1:'))
m1=int(input('digite m1:'))
a1=int(input('digite a1:'))
d2=int(input('digite d2:'))
m2=int(input('digite m2:'))
a2=int(input('digite a2:'))
if a1>a2:
    print("data1")
elif a1<a2:
    print("data2")
else:
    if m1>m2:
        print("data1")
    elif m1<m2:
        print("data2")
    else:
        if d1>d2:
            print("data1")
        elif d1<d2:
            print("data2")
        else:
            print("iguais")

