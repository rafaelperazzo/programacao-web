# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a==b and a==c and b==c:
    print('iguais')
elif a==b or a==c or b==c:
    print('dois numeros iguais')
else: print('diferentes')