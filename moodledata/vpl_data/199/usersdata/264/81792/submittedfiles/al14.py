# -*- coding: utf-8 -*-
n= int(input('Digite a quantidade de pessoas:'))
a=0
for i in range (0,n,1):
    idade= int(input('Digite a idade:'))
    a= a + idade
media= a/n
print ('%.2f' %media)