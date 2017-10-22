# -*- coding: utf-8 -*-
#ENTRADA
bin=int(input('Digite a entrada em 0s e 1s: '))
num = 0
cont = 0
#PROCESSAMENTO
while (bin>0) :
    num = num+((bin%10)**cont)
    bin = bin//10
    cont = cont+1
print(num)
    


