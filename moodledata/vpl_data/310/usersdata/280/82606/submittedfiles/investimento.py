# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
inv=float(input("Valor inicial do investimento: "))
tax=float(input("Taxa de crescimento percentual: "))
cont=0
while cont < 10:
    inv=inv+(tax*inv)
    print('%.2f' %(inv))
    cont=cont + 1
