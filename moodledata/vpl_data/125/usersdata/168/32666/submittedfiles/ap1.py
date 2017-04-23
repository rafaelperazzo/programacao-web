# -*- coding: utf-8 -*-
n1=float(input('Digite o número: '))
n2=float(input('Digite o número: '))
n3=float(input('Digite o número: '))
if n1<n2 and n2<n3:
    print(n3)
    print(n2)
    print(n1)
if n1<n3 and n3>n2:
    print(n2)
    print(n3)
    print(n1)
if n2<n3 and n3>n1:
    print(n1)
    print(n3)
    print(n2)
if n2>n1 and n1<n3:
    print(n3)
    print(n1)
    print(n2)
if n3>n2 and n2>n1:
    print(n1)
    print(n2)
    print(n3)
if n3>n1 and n1<n2:
    print(n2)
    print(n1)
    print(n3)