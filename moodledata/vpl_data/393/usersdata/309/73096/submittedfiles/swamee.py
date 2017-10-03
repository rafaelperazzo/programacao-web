# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("Digite um valor f:\n"))
l=float(input("Digite o valor de L:\n"))
q=float(input("Digite o valor de Q:\n"))
h=float(input("Digite o valor do delta H:\n "))
v=float(input("Digite o valor de v:\n"))

j=math.pi

d= ((8*f*l*q*q)/(h*9.81*j*j))
d= d**0.2

rey=(4*q)/(j*d*v)
p= ( 0.000002/(3.7*d)) + (5.74/(rey**0.9))
t= math.log10(p)
k= 0.25 / (t**2)

print("Para os valores fornecidos tem-se D sendo igual %.4f , Rey igual %.4f e k igual a %.4f" % (d, rey, k))