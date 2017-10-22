# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

reais = float(input('Digite o valor de reais: '))

quant20 = reais//20
resto20 = reais - (quant20*20)

quant10 = resto20//10
resto10 = resto20 - (quant10*10)

quant5 = resto10//5
resto5 = resto10 - (quant5*5)

quant2 = resto5//2
resto2 = resto5 - (quant2*2)

quant1 = resto2//1

print ('%.d' %quant20)
print ('%.d' %quant10)
print ('%.d' %quant5)
print ('%.d' %quant2)
print ('%.d' %quant1)