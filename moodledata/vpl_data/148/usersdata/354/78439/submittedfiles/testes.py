# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite o a: '))
b=int(input('digite o b: '))
c=int(input('digite o c: '))

if a<b<c:
    print('comando 1')
else:
    if a<c<b:
        print('comando 2')
    else:
        print('comando 3')
    print('comando 4')
print('pronto!')