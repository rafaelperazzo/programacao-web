# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
FT= float(input("Força de atrito inicial:"))
DH= float(input("perda de carga:"))
L= float(input("comprimento da tubulação:"))
Q= float(input("vazão:"))
g= float(input("gravidade:"))
V= float(input("Viscosidade cinemática:"))
E= float(input("Rugosidade do Tubo"))
Erro=1
for i in range(1,11,10):
    D=((8*FT*L*(Q**2))/(math.pi*g*DH))**(1/5)
    REY=(4*Q)/(D*V*math.pi)
    F=(((64/REY)**8)+9.5*((math.log(E/(3.7* D)+(5.74/((REY)**0.9)))-(2500/REY)**6)**(-16)))**0.125
    A=FT
    FT=F
    Erro=FT-A
    if Erro<0:
        Erro=Erro*(-1)
print('F= %f'%F )
print('REY= %f'%REY )
print('D= %f'%D )
if REY <= 2000:
    print("escoamento Laminar")
else:
    print("Escoamento Turbulento")