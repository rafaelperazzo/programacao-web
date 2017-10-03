# -*- coding: utf-8 -*-
dia=int(input("digite um dia:"))
mes=int(input("digite um mês:"))
ano=int(input("digite um ano:"))

dia2=int(input("digite um dia:"))
mes2=int(input("digite um mês:"))
ano2=int(input("digite um ano:"))
if ano==ano2 and mes==mes2 and dia==dia2:
    print('IGUAIS')
if ano>=ano2 and mes>=mes2 and dia>=dia2:
    print('DATA 1')
else :
    print('DATA 2')