# -*- coding: utf-8 -*-
x= int(input('Digite um valor com oito casas decimais: '))
y= 10000000
z= 100000000
soma= 0

while (True):
    if x<y:
        print('NAO SEI')
        break
    if x>z:
        print('NAO SEI')
        break
    if x>y or x<z:
        while x:
            soma += x%10
            x//=10
        print(soma)
        break