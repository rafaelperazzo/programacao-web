# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
#menor 
#maior
#a maior e e menor
if (a>b) and (a>c) and (a>d) and (a>e) and (e<b) and (e<c) and (e<d):
    print (e)
    print (a)
#a maior e d menor
elif (a>b) and (a>c) and (a>d) and (a>e) and (d<b) and (d<c) and (d<e):
    print (d)
    print (a)
#a maior e c menor
elif (a>b) and (a>c) and (a>d) and (a>e) and (c<b) and (c<d) and (c<e):
    print (a)
    print (c)
#a maior e b menor
elif (a>b) and (a>c) and (a>d) and (a>e) and (b<c) and (b<d) and (b<e):
    print (a)
    print (b)

#b maior e e menor
if (b>a) and (b>c) and (b>d) and (b>e) and (e<a) and (e<c) and (e<d):
    print (b)
    print (e)
#b maior e d menor
elif (b>a) and (b>c) and (b>d) and (b>e) and (d<a) and (d<c) and (d<e):
    print (b)
    print (d)
#b maior e c menor
elif (b>a) and (b>c) and (b>d) and (b>e) and (c<a) and (c<d) and (c<e):
    print (b)
    print (c)
#b maior e a menor
elif (b>a) and (b>c) and (b>d) and (b>e) and (a<c) and (a<d) and (a<e):
    print (b)
    print (a)
    
#c maior e e menor
if (c>a) and (c>b) and (c>d) and (c>e) and (e<a) and (e<b) and (e<d):
    print (c)
    print (e)
#c maior e d menor
elif (c>a) and (c>b) and (c>d) and (c>e) and (d<a) and (d<b) and (d<e):
    print (c)
    print (d)
#c maior e b menor
elif (c>a) and (c>b) and (c>d) and (c>e) and (b<a) and (b<d) and (d<e):
    print (c)
    print (b)
#c maior e a menor
elif (c>a) and (c>b) and (c>d) and (b>e) and (e<c) and (e<d) and (e<b):
    print (c)
    print (a)
    
#d maior e e menor
if (d>a) and (d>b) and (d>c) and (d>e) and (e<a) and (e<b) and (e<c):
    print (d)
    print (e)
#d maior e b menor
elif (d>a) and (d>b) and (d>c) and (d>e) and (b<a) and (b<c) and (b<e):
    print (d)
    print (d)
#d maior e c menor
elif (d>a) and (d>b) and (d>c) and (d>e) and (c<a) and (c<b) and (c<e):
    print (d)
    print (c)
#d maior e a menor
elif (d>a) and (d>b) and (d>c) and (d>e) and (a<c) and (a<e) and (a<b):
    print (d)
    print (a)
    
#e maior e b menor
if (e>a) and (e>b) and (e>d) and (e>c) and (b<a) and (b<c) and (b<d):
    print (e)
    print (e)
#e maior e d menor
elif (e>a) and (e>b) and (e>d) and (e>c) and (d<a) and (d<c) and (d<b):
    print (e)
    print (d)
#e maior e c menor
elif (e>a) and (e>b) and (e>d) and (e>c) and (c<a) and (c<b) and (c<d):
    print (e)
    print (c)
#e maior e a menor
elif (e>a) and (e>b) and (e>d) and (e>c) and (a<c) and (a<d) and (a<b):
    print (e)
    print (a)    