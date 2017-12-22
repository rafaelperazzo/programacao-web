# -*- coding: utf-8 -*-
import math
n = int(input('Digite a quantidade de múltiplos desejadas: '))
while n <= 0:
    n = int(input('Digite a quantidade de múltiplos desejadas: '))
a = int(input('Digite o primeiro número: '))
while a <= 0:    
    a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
while b <= 0:
    b = int(input('Digite o segundo número: '))
cont = 0
i = 1
while cont < n:
    if i%a == 0 or i%b == 0:
        print(i)
        cont += 1
    i += 1    

