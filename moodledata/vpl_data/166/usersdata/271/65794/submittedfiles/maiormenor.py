# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#PROCESSAMENTO
if (a>b) and (b>c) and (c>d) and (d>e) :
    print(a)
    print(e)
if (a>b) and (b<c) and (c>d) and (d>e) and (b>e) :
    print(a)
    print(e)
if (a>c) and (c>b) and (b>d) and (d>e) :
    print(a)
    print(e)
if (a>c) and (c<b) and (b>d) and (d>e) and (c>e) :
    print(a)
    print(e)
if (a>d) and (d>b) and (b>c) and (c>e) :
    print(a)
    print(e)
if (a>d) and (d<b) and (b>c) and (c>e) and (d>e) :
    print(a)
    print(e)
if (a>e) and (e>b) and (b>c) and (c>d) :
    print(a)
    print(d)
if (a>e) and (e<b) and (b>c) and (c>d) and (e>d) :
    print(a)
    print(e)
if (b>a) and (a>c) and (c>d) and (d>e) :
    print(b)
    print(e)
if (b>a) and (a<c) and (c>d) and (d>e) and (a>e) :
    print(b)
    print(e)
if (b>c) and (c>a) and (a>d) and (d>e) :
    print(b)
    print(e)
if (b>c) and (c<a) and (a>d) and (d>e) and (c>e) :
    print(b)
    print(e)
if (b>d) and (d>a) and (a>c) and (c>e) :
    print(b)
    print(e)
if (b>d) and (d<a) and (a>c) and (c>e) and (d>e) :
    print(b)
    print(e)
if (b>e) and (e>a) and (a>c) and (c>d) :
    print(b)
    print(d)
if (b>e) and (e<a) and (a>c) and (c>d) and (e>d):
    print(b)
    print(d)
if (c>a) and (a>b) and (b>d) and (d>e) :
    print(c)
    print(e)
if (c>a) and (a<b) and (b>d) and (d>e) and (a>e) :
    print(c)
    print(e)
if (c>b) and (b>a) and (a>d) and (d>e) :
    print(c)
    print(e)
if (c>b) and (b<a) and (a>d) and (d>e) and (b>e):
    print(c)
    print(e)
if (c>d) and (d>a) and (a>b) and (b>e) :
    print(c)
    print(e)
if (c>d) and (d<a) and (a>b) and (b>e) and (d>e) :
    print(c)
    print(e)
if (c>e) and (e>a) and (a>b) and (b>d) :
    print(c)
    print(d)
if (d>a) and (a>b) and (b>c) and (c>e) :
    print(d)
    print(e)
if (d>a) and (a<b) and (b>c) and (c>e) and (a>e) :
    print(d)
    print(e)
if (d>b) and (b>a) and (a>c) and (c>e) :
    print(d)
    print(e)
if (d>b) and (b<a) and (a>c) and (c>e) and (b>e) :
    print(d)
    print(e)
if (d>c) and (c>a) and (a>b) and (b>e) :
    print(d)
    print(e)
if (d>c) and (c<a) and (a>b) and (b>e) and (c>e) :
    print(d)
    print(e)
if (d>e) and (e>a) and (a>b) and (b>c) :
    print(d)
    print(c)
if (d>e) and (e<a) and (a>b) and (b>c) :
    print(d)
    print(c)
if (e>a) and (a>b) and (b>c) and (c>d) :
    print(e)
    print(d)
if (e>a) and (a<b) and (b>c) and (c>d) and (a>d) :
    print(e)
    print(d)
if (e>b) and (b>a) and (a>c) and (c>d) :
    print(e)
    print(d)
if (e>b) and (b<a) and (a>c) and (c>d) and (b>d) :
    print(e)
    print(d)
if (e>c) and (c>a) and (a>b) and (b>d) :
    print(e)
    print(d)
if (e>c) and (c<a) and (a>b) and (b>d) and (c>d) :
    print(e)
    print(d)
if (e>d) and (d>a) and (a>b) and (b>c) :
    print(e)
    print(c)
if (e>d) and (d<a) and (a>b) and (b>c) and (d>c) :
    print(e)
    print(c)