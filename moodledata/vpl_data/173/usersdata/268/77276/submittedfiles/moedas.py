# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input(' Digite o valor da cédula: '))

if (a>b):
    troca_a = n//a
    n=n//a
    troca_b = n//b
    if ((troca_a) == int(troca_a)) and ((troca_b) == int(troca_b)):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
else:
    troca_b = n//b
    n=n//b
    troca_a = n//a
    if ((troca_b) == int(troca_b)) and ((troca_a) == int(troca_a)):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
    