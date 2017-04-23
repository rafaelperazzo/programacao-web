# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=3.33*(10**53)
b=3*(10**11)
c=-2.25*(10**22)
delta=(b**2)-4*a*c
if delta>=0:
    x=(-b+(delta**0.5))/(2*a)
    x2=(-b-(delta**0.5))/(2*a)
    print(x)
    print(x2)
else:
    print('NO')
    
    
    
    