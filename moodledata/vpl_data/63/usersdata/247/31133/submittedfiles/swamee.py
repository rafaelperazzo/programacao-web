# -*- coding: utf-8 -*-
import math
f=float(input('digite f'))   
l=float(input('digite l'))
q=float(input('digite q'))
h=float(input('digite variaçao de H'))
v=float(input('digite v'))
g=9.81
e=0.000002
r=3.14
d=((8*f*l*q*q)/(r*g*h*r))**1/5
rey=4*q/r*d*v
k=0.25/(math.log(e/0.37*d+5.74/rey**0.9))**2
print(d)
print
print