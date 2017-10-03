# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
a= int(input('Digite a: '))
b= int(input('Digite b: '))
c= int(input('Digite c: '))

#CALCULO DO DELTA
delta = b * b - 4 * a * c

#Raizes
if delta<0 :
    print('SRR')

else :
    if delta>=0 :
        x1= (-b + delta ** (1/2))/2*a
        x2= (-b - delta ** (1/2))/2*a
        print('X1=%.2f' % x1)
        print('X2=%.2f' % x2)