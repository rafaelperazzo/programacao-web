# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO



n=int(input('n:'))

a=(n//10000000)
n3 = a
b=(n//1000000)
n1 = b - 10*a
c=(n//100000)
n2 = c -10*b

print(n1 + n2 + n3)
'''
if n < 10000000:
    print('NAO SEI')
elif n > 99999999:
    print('NAO SEI')
elif n%11111111==0:
    j = n//11111111
    j = j*8
    print(j)
elif 

'''