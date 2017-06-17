# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
DH= float(input("perda da carga:"))
L= float(input("comprimento da tubulação:"))
D= float(input("Diâmetro da tubulação:"))
E=float(input("Rugosidade do Tubo"))
V= float(input("Viscosidade cinemática:"))
FT=0.01
F=0
A=0
while A!= FT:
    Q=(((D*5)*DH)/0.08227*FT)**(1/2)
    F=(((64/REY)**8)+9.5*(math.log((E/(3.7*d))+(5.74/((REY)**0.9)))-(2500/REY)**6)**(-16))**0.125
    A=FT
    FT=F
print('F= %f'%F)
print('Q= %f'%Q)
if REY <= 2000:
    print("escoamento Laminar")
else:
    print("Escoamento Turbulento")