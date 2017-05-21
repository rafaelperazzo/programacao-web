# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s=float(input('Peso do peixe:'))
if s>50:
    excesso=s-50
    multa=(s/4)-12.5
    print('multa de:' %multa)
    print('excesso de:' %excesso)
elif s<=50:
    print('Excesso: 0')
    print('Multa 0')