# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
DH= float(input("perda de carga:"))
L= float(input("comprimento da tubulação:"))
Q= float(input("vazão:"))
g= float(input("gravidade:"))
E= float(input("Rugosidade do Tubo"))
V= float(input("Viscosidade cinemática:"))
FT=0.01
Erro=1
while Erro>0.000001:
    D=((8*f*L*(Q**2))/(math.pi*g*DH))**(1/5)
    REY=(4*Q)/(D*V*math.pi)
    F=(((64/REY)**8)+9.5*((math.log(E/(3.7* D)+(5.74/((REY)**0.9)))-(2500/REY)**6)**(-16)))**0.125
    A=FT
    FT=F
    Erro=FT-A
    if Erro<0:
        Erro=Erro*(-1)
print('F= %f'%F )
print('Q= %f'%Q )
if REY <= 2000:
    print("escoamento Laminar")
else:
    print("Escoamento Turbulento")