# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de termos:'))
pi = 1
numerador = 2
denominador = 1
i = 1
while i<=n:
       s=s*(numerador/denominador)
       
pi=2*s
print('%.5f' %pi)