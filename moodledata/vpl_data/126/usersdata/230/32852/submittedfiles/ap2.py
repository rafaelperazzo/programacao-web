# -*- coding: utf-8 -*-
n1=float(input('Digite Número 1: '))
n2=float(input('Digite Número 2: '))
n3=float(input('Digite Número 3: '))
n4=float(input('Digite Número 4: '))
if n1>n2 and n2>n3 and n3>n4:
    print(n1)
    print(n4)
elif n1>n3 and n3>n4 and n4>n2:
    print(n1)
    print(n2)
elif n1>n4 and n4>n2 and n2>n3:
    print(n1)
    print(n3)
elif n2>n1 and n1>n3 and n3>n4:
    print(n2)
    print(n4)
elif n2>n3 and n3>n4 and n4>n1:
    print(n2)
    print(n1)
elif n2>n4 and n4>n2 and n2>n3:
    print(n2)
    print(n3)
elif n3>n1 and n1>n2 and n2>n4:
    print(n3)
    print(n4)
elif n3>n2 and n2>n4 and n3>n1:
    print(n3)
    print(n1)
elif n3>n4 and n4>n1 and n1>n2:
    print(n3)
    print(n2)