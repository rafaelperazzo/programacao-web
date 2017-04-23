# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos:'))
denominator=1
numerator=2
term=1
product=1
while term<=n:
    product=product*(numerator/denominator)
    if numerator<denominator:
        numerator=numerator+2
    else:
        denominator=denominator+2
    term=term+1
result=product*2
print('pi=%.5f'% result)