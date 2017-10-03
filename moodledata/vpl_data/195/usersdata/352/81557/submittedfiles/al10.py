# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos:'))

numerador=2
denominador=1
s=1
i=1
j=0
while n>0:
    if i%2==0:
        num=(numerador-2)/denominador
    else:
        num=(numerador-j)/(denominador-j)
        s=s*num
    numerador=numerador+2
    denominador=denominador+2
    i=i+1
    j=j+2
    n=n-1
    
print(s)
pi=2*s
print('%.5f'%pi)