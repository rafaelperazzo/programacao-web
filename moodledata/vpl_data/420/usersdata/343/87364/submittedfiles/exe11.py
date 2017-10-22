# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))

soma = 0
while (n > 0) :
    if (n>=10000000 and n<=99999999) :
        resto=n//10
        n=(n-resto)/10
        soma=soma+resto
        print(n)
        break
    else :
        print('NAO SEI')
        break