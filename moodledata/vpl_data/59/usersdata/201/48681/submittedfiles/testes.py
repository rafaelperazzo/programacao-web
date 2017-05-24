# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('Digite um valor:'))
b=float(input('Digite um valor:'))
c=float(input('Digite um valor:'))
if a>b and a>c:
    print('MAIOR:' '%.f' %a)
    if a<b and a>c:
        print('INTER:' '%.f' %a)
    else:
        print('MENOR:' '%.f' %a)
elif b>a and b>c:
    print('MAIOR:' '%.f' %b)
    if b<a and b>c:
        print('INTER:' '%.f' %b)
    else:
        print('MENOR:' '%.f' %b)
    