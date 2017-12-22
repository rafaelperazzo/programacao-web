1# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

nome= input('digite seu nome: ')
num = input('digite um número: ')

import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print(nome + ' é gay por escolher o' + num)
