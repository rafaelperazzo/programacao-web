# -*- coding: utf-8 -*-

n=int(input('n:'))

    if n < 10000000:
        print('NAO SEI')
    elif n > 99999999:
        print('NAO SEI')
    elif n%11111111==0:
        j = n//11111111
        j = j*8
        print(j)
    else: 
        a=(n//10000000)
        n1 = a
        b=(n//1000000)
        n2 = b - 10*a
        c=(n//100000)
        n3 = c -10*b
        d = (n//10000)
        n4 = d - 10*c
        e = (n//1000)
        n5 = e - 10*d
        f = (n//100)
        n6 = f - 10*e
        g = (n//10)
        n7 = g - 10*f
        n8= n -10*g
        print(n1 + n2 + n3+n4 + n5 + n6+n7 + n8)
