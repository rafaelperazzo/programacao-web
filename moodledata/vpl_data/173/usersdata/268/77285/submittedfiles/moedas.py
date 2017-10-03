# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))

if (a>=b):
    troca_a = c//a
    c=c%a
    troca_b = c//b
    if ((troca_a) == int(troca_a)) and ((troca_b) == int(troca_b)):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
else:
    troca_b = c//b
    c=c%b
    troca_a = c//a
    if ((troca_b) == int(troca_b)) and ((troca_a) == int(troca_a)):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
    