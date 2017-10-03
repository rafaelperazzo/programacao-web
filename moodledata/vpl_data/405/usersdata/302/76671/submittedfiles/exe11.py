# -*- coding: utf-8 -*-
n = int(input('DIgite um número de 8 algarismos: '))

if n < 9999999:
    print('NÃO SEI')
else:
  soma = n*(n+1)//2
  print(soma)
