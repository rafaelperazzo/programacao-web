# -*- coding: utf-8 -*-
import math
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))
w = int(input("Digite o valor de w: "))
X=0
Y=0
Z=0
W=0
if x>y:
    X=1
if y>x and y>z:
    Y=1
if z>y and z>w:
    Z=1
if w>z:
    W=1
SOMA = X+Y+Z+W
if SOMA==1:
    print("S")
else:
    print("N")



