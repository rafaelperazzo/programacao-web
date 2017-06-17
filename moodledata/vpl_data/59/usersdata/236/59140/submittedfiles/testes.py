# -*- coding: utf-8 -*-
import math
DH= float(input('perda de carga:'))
L= float(input('comprimento da tubulação:'))
D= float(input('Diâmetro da tubulação:'))
E= float(input('Rugosidade do Tubo:'))
V= float(input('viscosidade cinemática:'))
FT= 0.01
F=0
A=0

while E>0.000001 :
    Q= (((D*5)*DH)/0.08227*L*FT)**(1/2)
    REY= (4*Q)/(D*V*math.pi)
    F= (((64/REY)**8) + 9.5 *(math.log ((E/(3.7*D)) + (5.74/((REY)**0.9))) - (2500/REY)**6)**(-16))**0.125
    A=FT 
    FT=F
    E=FT-A
    if E<0:
        E=E*(-1)
 
print('F= %f'%F)
print('Q= %f'%Q)
if REY<=2000:
    ('Escoamento Laminar')
else:
    print('Escoamento Turbulento')
    