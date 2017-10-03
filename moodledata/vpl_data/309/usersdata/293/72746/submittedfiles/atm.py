# -*- coding: utf-8 -*-
from __future__ import division
import math

dinheiro=int(input("Digite um valor: "))
divisao1=dinheiro//20
resto1=dinheiro%20
divisao2=resto1//20
resto2=resto1%20
divisao3=resto2//20
resto3=resto2%20
divisao4=resto3//20
resto4=resto3%20
divisao5=resto4//20
if type(dinheiro) is int:
    print(divisao1)
    print(divisao2)
    print(divisao3)
    print(divisao4)
    print(divisao5)