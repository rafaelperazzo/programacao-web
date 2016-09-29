# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

vi = input("Valor Inicial: ")
tx = input("Taxa Anual: ")

a1 = vi+(tx*vi)
a2 = a1+(tx*a1)

print("%.2f" %a1)
print("%.2f" %a2)