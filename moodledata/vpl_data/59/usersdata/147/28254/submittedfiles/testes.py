# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input("type a:"))
b=float(input("type b:"))
c=float(input("type c:"))
dt=(b*b)-(4*a*c)
if dt<0 :
    print("delta negetivo, nao existem raizes reais")
    sys.exit()
else: print("o valor de delta eh %.2f" %dt)
x1=(-b+(dt**0.5))/(2*a)
x2=(-b-(dt**0.5))/(2*a)
print('x1 é %.2f' %x1)
print('x2 é %.2f' %x2)