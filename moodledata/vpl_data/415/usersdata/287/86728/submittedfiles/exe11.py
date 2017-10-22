# -*- coding: utf-8 -*-
x=float(input('Escreva um numero com oito algaismos: '))
if x<9999999 and x<99999999:
    print('NAO SEI')
else:
    soma=0
    while (x>0):
        resto=x%10
        x=(x - resto)/10
        soma=soma+resto
    print('%.f' % soma)
    