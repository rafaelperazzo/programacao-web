# -*- coding: utf-8 -*-
"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento.

TEMPO ESTIMADO: 15 minutos
"""
popA = 80000
taxaA = 0.03
popB = 200000
taxaB = 0.015
anos = 0
while (popA < popB):
    popA = popA * (1 + taxaA)
    popB = popB * (1 + taxaB)
    anos = anos + 1
print(anos)