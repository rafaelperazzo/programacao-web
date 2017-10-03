# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))

if (a>=b):
    troca_a = c//a
    c1=c%a
    troca_b = c1//b
    if ((troca_a) == c/a ) and ((troca_b) == c1/b):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
else:
    troca_b = c//b
    c1=c%b
    troca_a = c1//a
    if ((troca_b) == c/b  ) and ((troca_a) == c1/a ):
        print(troca_a)
        print(troca_b)
    else:
        print('N')
    