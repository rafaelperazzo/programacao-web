# -*- coding: utf-8 -*-
bin = int(input("Digite a entrada em 0s e 1s: "))
num = 0
cont = 0
while (bin>0):
    ultimo = bin%10
    num = num+ultimo*(2**cont)
    cont = cont+1
    bin + bin//10
print(num)

