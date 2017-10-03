# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x1=('cedulas de 20')
x2=('cedulas de 10')
x3=('cedulas de 5')
x4=('cedulas de 2')
x1=('cedulas de 1')
v=int(input('Digite o valor a ser sacado:'))
x1=((v//20))
print(x1)
if ((v//20)<1):
qtinicial50 = 10
qtinicial20 = 10
qtinicial10 = 10
qtinicial5 = 10
qt50 = 500
qt20 = 200
qt10 = 100
qt5 = 50

totalcaixa = qt50 + qt20 + qt10 + qt5

notasrestantes50 = 10
notasrestantes20 = 10
notasrestantes10 = 10
notasrestantes5 = 10

while True:
    val = input("Digite o valor para saque: ")
    if type (val) is float: #verifica se o conteudo de val é float
        print "Não aceito valores com centavos"
        continue

    if val > totalcaixa:
        print "O caixa eletronico não possui este valor"
        continue

    if val % 5 > 0 or val <= 0: # o caixa nao possui notas de 1 e 2, este if limita valores como 51 por exemplo ou 52
        print "erro"
        continue # retorna o programa para o inicio do while
   
    not50 = val / 50
    val   = val % 50
    not20 = val / 20
    val   = val % 20
    not10 = val / 10
    val   = val % 10
    not5  = val / 5
    val   = val % 5


    print "Este valor corresponde a: "
    if not50 > 0: print not50," notas de R$ 50,00"
    if not20 > 0: print not20," notas de R$ 20,00"
    if not10 > 0:print not10," notas de R$ 10,00"
    if not5 > 0:print not5," notas de R$ 5,00"