# -*- coding: utf-8 -*-
import math
#Entrada:
a= float(input('Digite o valor de a:'))
b= float(input('Digite o valor de b:'))
c= float(input('Digite o valor de c:'))
d= float(input('Digite o valor de d:'))
#Processamento e Saída:
if (a>b) and (b>c) and (c>d):
    print ('S')
elif (a>b) and (b==c) and (c==d):
    print ('S')
elif (a>b) and (a==c) and (c==d):
    print ('S')
elif (d>c) and (c>b) and (b>a):
    print ('S')
elif (d>c) and (c==d) and (b==a):
    print ('S')
elif (d>c) and (b==d) and (b==a):
    print ('S')
elif (b>a) and (b>c) and (c>a) and (d<a):
    print ('S')
elif (b>a) and (b>c) and (a<c) and (d<a):
    print ('S')
elif (b>a) and (b>c) and (c>a) and (a==d):
    print ('S')
elif (b>a) and (b>c) and (c<a) and (d<c):
    print ('S')
elif (b>a) and (b>c) and (d<c) and (c==a):
    print ('S')
elif (b>a) and (b>c) and (a<c) and (c==d):
    print ('S')
elif (b>a) and (b>c) and (c<a) and (c==d):
    print ('S')
elif (b>a) and (a==c) and (c==d):
    print ('S')
elif (c>d) and (c>b) and (d<b) and (a<d):
    print ('S')
elif (c>d) and (c>b) and (d<b) and (a<b):
    print ('S')
elif (c>d) and (c>b) and (a<b) and (a==d):
    print ('S')
elif (c>d) and (c>b) and (b<d) and (a<b):
    print ('S')
elif (c>d) and (c>b) and (a<b) and (b==d):
    print ('S')
elif (c>b) and (c>d) and (d<b) and (b==a):
    print ('S')
elif (c>d) and (c>b) and (a<d) and (a==b):
    print ('S')
elif (c>d) and (c>b) and (a==b) and (b==d):
    print ('S')
else:
    print ('N')