# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

R1=c//a
resto1=c%a

if resto1!=0:
    R2=resto1//b
    resto2=resto1%b
    if resto2==0:
        print ('%d' %R1)
        print ('%d' %R2)
    elif resto2!=0:
        R3=c//b
        resto3=c%b
        if resto3==0:
            print ('0')
            print ('%d' %R3)
        elif resto3!=0:
            R4= resto3//a
            resto4=resto3%a
            if resto4==0:
                print ('%d' %R4)
                print ('%d' %R3)
            else:
                print ('N')
elif resto1==0:
    print ('%d' %R1)
    print ('0')
        
