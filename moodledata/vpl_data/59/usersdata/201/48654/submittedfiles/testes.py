# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('Digite um valor:'))
b=float(input('Digite um valor:'))
c=float(input('Digite um valor:'))
if a>b and a>c:
    print('MAIOR: %a')
    if a<b and a>c:
        print('INTER: %a')
    else:
        print('MENOR: %a')