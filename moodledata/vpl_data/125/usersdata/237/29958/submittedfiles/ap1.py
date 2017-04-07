# -*- coding: utf-8 -*-
a=float(input("digite a: "))
b=float(input("digite b: "))
c=float(input("digite c: "))
if a>b and b>c:
    print("%.f" % a)
    print("%.f" % b)
    print("%.f" % c)
if a>b and c>a:
    print("%.f" % c)
    print("%.f" % a)
    print("%.f" % b)
if a<c and b>c:
    print("%.f" % b)
    print("%.f" % c)
    print("%.f" % a)