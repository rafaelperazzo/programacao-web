# -*- coding: utf-8 -*-
#ENTRADA
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
#PROCESSAMENTO
if a>b>c:
    print ('c')
    print ('b')
    print ('a')
if a>c>b:
    print ('b')
    print ('c')
    print ('a')
if b>c>a:
    print ('a')
    print ('c')
    print ('b')
if b>a>c:
    print ('c')
    print ('a')
    print ('b')
if c>a>b:
    print ('b')
    print ('a')
    print ('c')
if c>b>a:
    print ('a')
    print ('b')
    print ('c')