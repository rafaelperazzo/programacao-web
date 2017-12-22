# -*- coding: utf-8 -*-
import math
x=float(input("Digite o valor de x: "))
y=float(input("Digite o valor de y: "))
z=float(input("Digite o valor de z: "))
w=float(input("Digite o valor de w: "))
if x<y and y<z and z<w:
    print("S")
elif x<y and z<y and w<z:
    print("S")
elif y>x and z>y and z>w:
    print("S")
elif x>y and y>z and z>w:
    print("S")
elif x>y and y==z and z==w:
    print("S")
elif x==y and y==z and z<w:
    print("S")
elif x<y and y==z and z<w:
    print("S")
elif x>y and y==z and z>w:
    print("S")
elif x==y and y<z and z>w:
    print("S")
elif x>y and x==z and x==w:
    print("S")
else:
    print("N")
    
