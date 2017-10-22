# -*- coding: utf-8 -*-
a = int(input('Digite a:'))
b = int(input('Digite b:'))
c = int(input('Digite c:'))

i = 0

while (i<c):
    valora = i*a
    valorb = c - valora
    if (c%(valorb)==0):
        qa = c//i
        qb = valorb//b
        print (qa)
        print (qb)
        break
    else:
        print ('n')
    i = i +1

    
