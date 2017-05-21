# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s=float(input('Peso do peixe:'))
if s>50:
    exc=s-50
    m=(s/4)-12.5
    print('multa de:' %m)
    print('excesso de:' %exc)
elif s<=50:
    print('Excesso: 0')
    print('Multa 0')