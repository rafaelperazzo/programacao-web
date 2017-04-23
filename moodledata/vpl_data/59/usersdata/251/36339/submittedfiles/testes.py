# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = int(input('Digite o peso da esfera A: '))
b = int(input('Digite o peso da esfera B: '))
c = int(input('Digite o peso da esfera C: '))
d = int(input('Digite o peso da esfera D: '))

if a==b+c+d and b+c==d and b==c:
    print('S')
    
else:
    print('N')
        
        
