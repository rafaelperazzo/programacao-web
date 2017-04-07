# -*- coding: utf-8 -*-
print("Ordenamento de números:")
print("")
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
if a>b>c:
    print("%d"%c)
    print("%d"%b)
    print("%d"%a)
if a>c>b:
    print("%d"%b)
    print("%d"%c)
    print("%d"%a) 
if b>a>c:
    print("%d"%c)
    print("%d"%a)
    print("%d"%b)
if b>c>a:
    print("%d"%a)
    print("%d"%c)
    print("%d"%b)
if c>a>b:
    print("%d"%b)
    print("%d"%a)
    print("%d"%c)
if c>b>a:
    print("%d"%a)
    print("%d"%b)
    print("%d"%c)
if a==b==c:
    print("%d"%a)
    print("%d"%b)
    print("%d"%c)
