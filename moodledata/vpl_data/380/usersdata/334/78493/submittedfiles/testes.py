# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))

if a < b and a < c:
    print (a)
if a==b:
    if a < c:
        print (a)
if b < a and b < c:
    print (b)
if c < a and c < b:
    print (c)

if a > b and a < c or a < b and a > c:
    print (a)
if b > a and b < c or b < a and b > c:
    print (b)
if c > a and c < b or c < a and c > b:
    print (c)

if a > b and a > c:
    print (a)
if b > a and b > c:
    print (b)
if c > a and c > b:
    print (c)