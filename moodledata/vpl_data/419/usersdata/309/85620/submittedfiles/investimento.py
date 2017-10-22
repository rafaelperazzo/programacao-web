# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

valor = float(input ("Digite o valor do investimento inicial :"))
x =  float(input ("Taxa de crescimento precentual:"))

i=1

while (i< 11):
    valor=valor + x*valor
    print ("%.2f" %valor )
   
    i=i+1
    