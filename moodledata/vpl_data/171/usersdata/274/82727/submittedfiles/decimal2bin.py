# -*- coding: utf-8 -*-
#ENTRADA
bin = int(input("Digite a entrada em 0s e 1s:" ))
num = 0
cont = 0
#PROCESSAMENTO
while (bin>0) :
    ultimo = bin%10
    num = num+ultimo*(2**cont)
    cont = cont+1
    bin = bin//10
print(num)
