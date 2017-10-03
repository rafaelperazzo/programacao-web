# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("Digite um valor f:\n"))
l=float(input("Digite o valor de L:\n"))
q=float(input("Digite o valor de Q:\n"))
h=float(input("Digite o valor do delta H:\n "))
v=float(input("Digite o valor de v:\n"))

j=math.pi

d= ((8*f*l*q**2)/(h*9.81*j**2))**1/5
rey=4*q/j*d*v
k=0.25/math.log10(0.000002/3.7*d + 5.74/rey**0.9)**2

print("Para os valores fornecidos tem-se D sendo igual %.f , Rey igual %.f e k igual a %.f" % (d, rey, k))