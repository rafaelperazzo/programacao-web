# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

a1=input('digite a1:')
a2=input('digite a2:')
a3=input('digite a3:')
a4=input('digite a4:')
a5=input('digite a5:')
a6=input('digite a6:')
b1=input('digite b1:')
b2=input('digite b2:')
b3=input('digite b3:')
b4=input('digite b4:')
b5=input('digite b5:')
b6=input('digite b6:')

cont=0

if a1==b1 or a1==b2 or a1==b3 or a1==b4 or a1==b5 or a1==b6:
    cont=cont+1
   
if a2==b1 or a2==b2 or a2==b3 or a2==b4 or a2==b5 or a2==b6:
    cont=cont+1
    
if a3==b1 or a3==b2 or a3==b3 or a3==b4 or a3==b5 or a3==b6:
    cont=cont+1
    
if a4==b1 or a4==b2 or a4==b3 or a4==b4 or a4==b5 or a4==b6:
    cont=cont+1
    
if a5==b1 or a5==b2 or a5==b3 or a5==b4 or a5==b5 or a5==b6:
    cont=cont+1
    
if a6==b1 or a6==b2 or a6==b3 or a6==b4 or a6==b5 or a6==b6:
    cont=cont+1
    
if cont<3:
    print('azar')
    
if cont==3:
    print('terno')
    
if cont==4:
    print('quadra')
    
if cont==5:
    print('quina')
    
if cont==6:
    print('sena')


