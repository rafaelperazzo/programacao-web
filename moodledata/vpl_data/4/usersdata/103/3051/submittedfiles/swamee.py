# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('Insira F')
L=input('Insira L')
Q=input('Insira Q')
dH=input('Insira dH')
T=input('Insita teta')
G=9.81
E=0.000002
Pi=3.14
D1=(Pi**2)*G*dH
if D1!=0:
    D2=(8*F*L*(Q**2))/D1
    if D2>=0:
        D=(D2**0.2)
        If Pi*D*T!=0:
            Rey=(4*Q)/(Pi*D*T)
            R1=math.logo10((E/(3.7*D))+5.74/(Rey**0.9))
            If R1!=0:
                K=0,25/(R1**2)
                print('D=%.4f'%D)
                print('Rey=%.4f'%Rey)
                print('K=%.4f'%K)
            Else:
                print('D=%.4f'%D)
                print('Rey=%.4f'%Rey)
                print('K não possui valor real')
        Else:
            print('D=%.4f'%D)
            print('Rey não possui valor real')
            print('K não possui valor real')
    Else:
        print('Dnão possui valor real')
        print('Rey não possui valor real')
        print('K não possui valor real')
Else:
    print('Dnão possui valor real')
    print('Rey não possui valor real')
    print('K não possui valor real')            