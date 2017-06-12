# -*- coding: utf-8 -*-
import math
DH= float(input('perda de carga'))
L= float(input('comprimento da tubulação'))
D= float(input('Diâmetro da tubulação'))
V= float(input('viscosidade cinemática'))
E= float(input('Rugosidade do Tubo'))
ftest= 0.01

while true:
    Q= (((D*5)*DH)/0.08227*L*ftest)**(1/2)
    REY= (4*Q)/(D*V*math.pi)
    F= (((64/REY)**8) + 9.5 * (((log ((E/(3.75*D)) + (5.74/(REY**0.9))) - ((2500/REY)**6))**16))**0.125
    if ftest==F:
        print('%f'%F)
        print(Q)
        if REY<=2000:
            ('Escoamento Laminar')
        else:
            print('Escoamento Turbulento')
        break
    else:
        ftest=F



