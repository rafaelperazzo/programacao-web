# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um número:'))
num=2
den=1
i=1
termo=1
while=i<=n:
    termo=termo*(num/den)
    if den<num:
        den=den+2
    else:
        num=num+2
    i=i+1
termo=termo*2
print('%.5%' %termo)

