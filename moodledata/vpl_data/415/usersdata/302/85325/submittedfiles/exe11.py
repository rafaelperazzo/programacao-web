# -*- coding: utf-8 -*-
n = int(input('digite o valor de n: '))
if n > 9999999 and n <= 99999999:
    soma = 0
    while (n!=0):
        n = (n-resto)//10
        soma = soma + resto
    print(soma)
else:
    print('Não Sei')
    
