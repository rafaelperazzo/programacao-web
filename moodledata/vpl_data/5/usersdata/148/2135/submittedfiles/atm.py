# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
valor = int(input('Digite o valor do saque:'))
#PROCESSAMENTO
restoVinte = valor%20
restoDez = restovinte%10
restoCinco = restoDez%5
restoDois = restoCinco%2
restoUm = restoDois%1

qtdVinte = valor-restoVinte
qtdTotalVinte = qtdVinte/20

qtdDez = restoVinte-restoDez
qtdTotalDez = qtdDez/10

qtdCinco = restoDez-restoCinco
qtdTotalCinco = qtdCinco/5

qtdDois = restoCinco-restoDois
qtdTotalDois = qtdDois/2

qtdUm = restoDois-restoUm
qtdTotalUm = qtdUm/1

#SAIDA
print ('%d' %qtdTotalVinte)
print ('%d' %qtdTotalDez)
print ('%d' %qtdTotalCinco)
print ('%d' %qtdTotalDois)
print ('%d' %qtdTotalUm)