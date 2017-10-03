# -*- coding: utf-8 -*-
dia=int(input("digite um dia"))
mes=int(input("digite um mes"))
ano=int(input("digite um ano"))
dia2=int(input("digite um dia2"))
mes2=int(input("digite um mes2"))
ano2=int(input("digite um ano2"))
if ano==ano2 and mes==mes2 and dia==dia2:
    print('IGUAIS')
elif ano>=ano2 and mes>=mes2 and dia>=dia2:
    print('DATA 1')
else:
    print('DATA 2')
    
