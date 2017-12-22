# -*- coding: utf-8 -*-
n=int(inpt('quantidade de termos:'))

if n >= 2:
    a=[]
        for i in range (0, n, 1):
            a[i] = int(input())
        for i in range (0, n, 1):
            valor = abs(a[i] - a[i+1])
            print 'O degrau de'
            print a[i]
            print ' e '
            print a[i+1]
            print 'é igual a: '
            print (abs(a[i] - a[i+1))
            
            



