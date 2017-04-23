# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor a:'))
b=int(input('Digite o valor b:'))
c=int(input('Digite o valor c:'))
if a<b+c:
    print('S')
else:
    print('N')
    if a**2==b**2+c**2:
            print('Retângulo')
        elif a**2>b**2+c**2:
            print('Obtusângulo')
        elif a**2<b**2+c**2:
            print('Acutângulo')
                if a==b==c:
                    print('Equilatéro')
                elif a==b==!c:
                    print('Isósceles')
                elif a==!b==!c:
                    print('Escaleno')
else:
    print('N')
    