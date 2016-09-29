# -*- coding: utf-8 -*-
from __future__ import division
#Entrada

peso = input('Digite o peso: ')
altura = input('Digite a altura: ')

#PROCESSAMENTO

imc = peso / (altura**2)

#SAÍDA

if imc < 20:
    print "ABAIXO"
    
if (imc>=20) and (imc<=25):
    print "NORMAL"

if (imc>25) and (imc<=30):
    print "SOBREPESO"
    
if (imc>30) and (imc<=40):
    print "OBESIDADE"
    
if imc>40:
    print "OBESIDADE GRAVE"
    