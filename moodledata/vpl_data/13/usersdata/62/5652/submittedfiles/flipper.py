# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

#ENTRADA

P=input("Digite o valor de P: ")
R=input("Digite o valor de R: ")

#PROCESSAMENTO/SAIDA

if P==0:
    print("C")
elif P==1 and R==0:
    print("B")
elif P==1 and R==1:
    print("A")