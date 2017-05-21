# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
a=float(input("digite o valor do primeiro número:"))
b=float(input("digite o valor do segundo número:"))
c=float(input("digite o valor do último número:"))
if (a>b) and (a>c):
    if (b>c):
        print("a sequência é:" "%.f %.f %.f" %(a,b,c)
if (b>c) and (b>a):
    if (a<c):
        print("a sequência é:" "%.f %.f %.f" %(b,c,a)
if (c>b) and (c>a):
    if (b>a):
        print("a sequência é:" "%.f %.f %.f" %(c,b,a)