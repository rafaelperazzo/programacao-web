# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sb=float(input('digite o salario bruto:'))
vp=float(input('digite o valor da prestação:'))
if vp<=((30/100)*sb):
    print('emprestimo concedido')
else:
    print('emprestimo não concedido')


