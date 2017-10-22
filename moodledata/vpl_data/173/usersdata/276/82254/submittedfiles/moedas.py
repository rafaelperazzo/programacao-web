# -*- coding: utf-8 -*-
a = int(input('Digite a:'))
b = int(input('Digite b:'))
c = int(input('Digite c:'))

i = 0
contador = 0

while (i<c):
    valora = i*a
    valorb = c - valora
    if (valorb%b==0):
        qa = i
        qb = valorb//b
        print (qa)
        print (qb)
        break
    else:
        i = i +1
        contador = contador +1
        
if (contador!=0):
    print ('n')
    
