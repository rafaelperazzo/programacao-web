# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
DH= float(input("perda da carga:"))
L= float(input("comprimento da tubulação:"))
E=float(input("Rugosidade do Tubo"))
V= float(input("Viscosidade cinemática:"))
FT=0.01
F=0
A=0
While A!= FT:
    Q=(((D*5)*DH)/0.08227*FT)**(1/2)
    