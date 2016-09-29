# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#ENTRADA
inicial=input("investimento inicial: ")
taxa=input("taxa de crescimento percentual: ")
#PROCESSAMENTO
ano1=inicial+taxa*inicial
ano2=ano1+taxa*ano1
ano3=ano2+taxa*ano2
ano4=ano3+taxa*ano3
ano5=ano4+taxa*ano4
ano6=ano5+taxa*ano5
ano7=ano6+taxa*ano6
ano8=ano7+taxa*ano7
ano9=ano8+taxa*ano8
ano10=ano9+taxa*ano9
#SAIDA
print("resultados: ")
print("%2.f" ano1)
print(ano2)
print(ano3)
print(ano4)
print(ano5)
print(ano6)
print(ano7)
print(ano8)
print(ano9)
print(ano10)