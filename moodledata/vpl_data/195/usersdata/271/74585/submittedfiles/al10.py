# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
#ENTRADA
n = int(input('Digite o valor de n: '))
num = 2
den = 1
cont = 1
mult = 1
#PROCESSAMENTO
while (cont<=n) :
    mult = mult*(num/den)
    if (num/den) > 1 :
        den = den+2
    elif (num/den) < 1 :
        num = num+2
    cont = cont+1
pi = mult*2
print('O valor de pi é %.5f : ' % pi)
