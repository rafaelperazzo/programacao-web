# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
FT=float(input("Força de atrito inicial"))
DH=float(input("perda de carga:"))
L=float(input("comprimento da tubuação:"))
Q=float(input("Vazão:"))
g=float(input("gravidade:"))
E=float(input("Rugosidade do Tubo:"))
V=float(input("viscosidade:"))

Erro=1
for i in range(0,10,1):
    D=((8*FT*L*(Q**2))/(((math.pi)**2)*g*DH))**(1/5)
    REY=(4*Q)/(D*V*math.pi)
    F=(((64/(REY)**8)+9.5*(math.log(E/(3.7*D)+5.74/(REY**0.9))-(2500/REY)**6)**(-16)))**(0.125)
    A=FT
    FT=F
    Erro=FT-A
    if Erro<0:
        Erro=Erro*(-1)
print(F)
print(REY)
print(D)
if REY<=2000:
    print("escoamento laminar")
else:
    print("escoamento turbulento")
