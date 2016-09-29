# -*- coding: utf-8 -*-
from __future__ import division

#Entrada 

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

#Processamento

IMC = peso / (altura)**2

#Saída
 
if IMC < 20:
    print('Abaixo')
    
if 20 <= IMC <= 25:
    print('Normal')
    
if 25 < IMC <= 30:
    print('Sobrepese')
    
if 30 < IMC <= 40:
    print('Obesidade')
    
if IMC > 40:
    print('Obesidade Grave')
    
    