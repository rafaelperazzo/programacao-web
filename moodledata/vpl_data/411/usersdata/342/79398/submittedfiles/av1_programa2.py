# -*- coding: utf-8 -*-
x = float(input('Valor que consta na etiqueta:'))
y = int(input('Condição de pagamento:[1-4]'))

a = (x*0.85) 
b = (x*0.90)
c = (x*1.00)
d = (x*1.10)

if y==1:
    print (a)
if y==2:
    print (b)
if y==3:
    print (c)
if y==4:
    print (d)

