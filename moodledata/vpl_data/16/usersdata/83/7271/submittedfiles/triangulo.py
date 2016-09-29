# -*- coding: utf-8 -*-
from __future__ import division
import math


a=input('Digite o primeiro valor :')
b=input('Digite o segundo valor :')
c=input('Digite o terceiro valor :')

if a>=b>=c>0 and a<b+c :
    print ('S')
if a>=b>=c>0 and a<b+c :
        if ((a)**2)==((b)**2)+((c)**2):
            print ('Re')
        elif ((a)**2)>((b)**2)+((c)**2):
            print ('Ob')
        elif ((a)**2)<((b)**2)+((c)**2):
            print ('Ac')
if a>=b>=c>0 and a<b+c :
    if a==b==c :
        print ('Eq')
    elif a==b!=c or a!=b==c :
        print ('Is')
    elif a!=b!=c:
        print ('Es')
else :
    print ('N')
    