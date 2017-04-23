# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('Digite o número de termos: '))
pi=1
num=2
den=1
for i in range(1,n+1,1):
    
    if num>den:
        pi=pi*(num/den)
        den=den+2
    elif den>num:
        pi=pi*(num/den)
        num=num+2

print('%.5f'%(pi*2))        