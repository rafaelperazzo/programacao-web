# -*- coding: utf-8 -*-
import math

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))
c= int(input('Digite o valor de c: '))

if (a>(b+c)):
    print('N')

elif (a==(b+c)):
    print('N')
    
elif (a<(b+c)):
    print('S')
    
    if ((a*a)==((b*b)+(c*c))):
        print('Re')
    
    elif ((a*a)>((b*b)+(c*c))):
        print('Ob')
    
    elif ((a*a)<((b*b)+(c*c))):
        print('Ac')
    
    if (a==b==c):
        print('Eq')
    
    elif (b==c=!a):
        print('Is')
    
    elif (a=!b=!c):
        print('Es')
    
