# -*- coding: utf-8 -*-
a=float(input("digite a: "))
b=float(input("digite b: "))
c=float(input("digite c: "))
if c>b and b>a:
    print("%.f" % a)
    print("%.f" % b)
    print("%.f" % c)
if b>c and c>a:
    print("%.f" % a)
    print("%.f" % c)
    print("%.f" % b)
if a>c and c>b:
    print("%.f" % b)
    print("%.f" % c)
    print("%.f" % a)
if c>a and a>b:
    print("%.f" % b)
    print("%.f" % a)
    print("%.f" % c)
if b>a and a>c:
    print("%.f" % c)
    print("%.f" % a)
    print("%.f" % b)    
if a>b and b>c:
    print("%.f" % c)
    print("%.f" % b)
    print("%.f" % a)