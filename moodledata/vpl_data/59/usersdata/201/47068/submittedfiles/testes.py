# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s=float(input('Peso do peixe:'))
if s>50:
    exc=s-50
    m=exc*4
    print('excesso de:''%.2f' %exc)
     print('multa de:''%.2f' %m)
elif s<=50:
    print('Excesso: 0')
    print('Multa 0')