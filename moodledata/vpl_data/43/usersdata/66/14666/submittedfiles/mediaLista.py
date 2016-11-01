# -*- coding: utf-8 -*-
from __future__ import division
n=input ("digite a quantidade ne n:")
a=[]
for i in range(0,n,1):
    a.append(input("digite os valores: "))

i=0
soma=0
while i<n:
   soma=(soma+ a[i])
   i=i+1
media=((soma)/(len(a)))

print ("%.2f" %a[0])
print ("%.2f" %a[len(a)-1])
print("%.2f" %media)
print (a)