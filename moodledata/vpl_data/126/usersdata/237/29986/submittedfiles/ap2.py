# -*- coding: utf-8 -*-
a=float(input('digite a:))
b=float(input('digite b:))
c=float(input('digite c:))
d=float(input('digite d:))
if a>b and b>c and c>d:
    print("%.f" % a)
    print("%.f" % d)
if a>b and b>d and d>c:
    print("%.f" % a)
    print("%.f" % c)
if a>c and c>b and b>d:
    print("%.f" % a)
    print("%.f" % d)
if a>c and c>d and d>b:
    print("%.f" % a)
    print("%.f" % b)
if a>d and d>b and b>c:
    print("%.f" % a)
    print("%.f" % c)
if a>d and d>c and c>b:
    print("%.f" % a)
    print("%.f" % b)
if b>a and a>c and c>d:
    print("%.f" % b)
    print("%.f" % d)
if b>a and a>d and d>c:
    print("%.f" % b)
    print("%.f" % c)
if b>c and c>a and a>d:
    print("%.f" % b)
    print("%.f" % d)
if b>c and c>d and d>a:
    print("%.f" % b)
    print("%.f" % a)
if b>d and d>c and c>a:
    print("%.f" % a)
    print("%.f" % a)
if b>d and d>a and a>c:
    print("%.f" % b)
    print("%.f" % c)
if c>a and a>b and b>d:
    print("%.f" % c)
    print("%.f" % d)
if c>a and a>d and d>b:
    print("%.f" % c)
    print("%.f" % b)
if c>b and b>a and a>d:
    print("%.f" % c)
    print("%.f" % d)
if c>b and b>d and d>a:
    print("%.f" % c)
    print("%.f" % a)
if c>d and d>a and a>b:
    print("%.f" % c)
    print("%.f" % b)
if c>d and d>b and b>a:
    print("%.f" % c)
    print("%.f" % a)
if d>b and b>c and c>a:
    print("%.f" % d)
    print("%.f" % a)
if d>b and b>a and a>c:
    print("%.f" % d)
    print("%.f" % c)
if d>a and a>b and b>c:
    print("%.f" % d)
    print("%.f" % c)
if d>a and a>c and c>b:
    print("%.f" % d)
    print("%.f" % b)
if d>c and c>a and a>b:
    print("%.f" % d)
    print("%.f" % b)
if d>c and c>b and b>a:
    print("%.f" % d)
    print("%.f" % a)