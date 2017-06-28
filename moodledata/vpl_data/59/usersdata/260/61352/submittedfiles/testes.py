# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
FT=float(input("Digite o valor do fator de atrito inicial"))
DH=float(input("Digite o valor da perda de carga distribuída mensurada em metros:"))
L=float(input("Digite o valor do comprimento da tubuação:"))
Q=float(input("Digite o valor da vazão em metros cúbicos por segundo:"))
g=float(input("Digite o valor da aceleração gravitacional em metros por segundo ao quadrado:"))
E=float(input("Digite o valor da rugosidade do Tubo em metros:"))
V=float(input("Digite o valor da viscosidade cinemática a uma temperatura fixa em metros por segundo ao quadrado:"))

FT=0.2
DH=5
L=3250
Q=0.005
g=9.81
E=0.00006
V=0.000001

Erro=1
while Erro>0.000001:
    D=((8*FT*L*(Q**2))/(((math.pi)**2)*g*DH))**(1/5)
    REY=(4*Q)/(D*V*math.pi)
    F=(((64/(REY)**8)+9.5*(math.log(E/(3.7*D)+5.74/(REY**0.9))-(2500/REY)**6)**(-16)))**(0.125)
    A=FT
    FT=F
    Erro=FT-A
    if Erro<0:
        Erro=Erro*(-1)
print("F é igual a %.6f" %F)
print("D é igual a %.6f metros" %D)
print("REY é igual a %.6f" %REY)
if REY<=2000:
    print("O escoamento é classificado como laminar")
else:
    print("O escoamento  é classificado como turbulento")
