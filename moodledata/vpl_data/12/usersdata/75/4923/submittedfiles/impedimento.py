# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada 
L= input ('Digite a posição do atacante que lança a bola:')
R= input ('Digite a podição do atacante que recebe a bola:')
D= input ('Digite a posição do defensor:')

#Processamento e Saida

if (R>50) and (L<R) and (R>D):
    print ('S')
else:
    print ('N') 