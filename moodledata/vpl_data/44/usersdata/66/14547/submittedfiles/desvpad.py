# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input ("digite a quantidade ne n:")
a=[]
for i in range(0,n,1):
    a.append(input("digite os valores"))

i=0
soma=0
while i<n:
   soma=(soma+ a[i])
   i=i+1
media=((soma)/(len(a)))

soma=0
i=0
for i in range (0,n,1):
    soma=soma +(a[i]- media)**2
d=(1/(n-1)* (soma))**0.5
i=0
soma=0
while i<n:
   soma=(soma+ a[i])
   i=i+1
media=((soma)/(len(a)))

print ("%.2f" %a[0])
print ("%.2f" %a[len(a)-1])
print("%.2f" %media)
n=input ("digite a quantidade ne n:")
a=[]
for i in range(0,n,1):
    a.append(input("digite os valores"))

i=0
soma=0
while i<n:
   soma=(soma+ a[i])
   i=i+1
media=((soma)/(len(a)))

print ("%.2f" %a[0])
print ("%.2f" %a[len(a)-1])
print("%.2f" % d)
print (a)
print (a)