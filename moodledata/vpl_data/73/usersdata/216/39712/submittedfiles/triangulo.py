# -*- coding: utf-8 -*-
import math
a=int(input('Digite o comprimento a:'))
b=int(input('Digite o comprimento b:'))
c=int(input('Digite o comprimento c:'))

if a<(b+c):
    if (a**2)==((b**2)+(c**2)):
        print('Retângulo')
    if (a**2)>((b**2)+(c**2)):
        print('Obtusângulo')
    if (a**2)<((b**2)+(c**2)):
        print('Acutângulo')
        
    if a==b and b==c:
        print('Equilátes')
    if b==c and c!=a:
        print('Isoceles')
    if a!=b and b!=c:
        print('Escaleno')
        
else:
    print('Não é um triangulo')