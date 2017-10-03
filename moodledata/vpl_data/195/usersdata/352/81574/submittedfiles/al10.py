# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos:'))

numerador=0
denominador=0
s=1
i=1

while i<n:
    if i%2==0:
        s=s*(numerador/denominador)
    else:
        s=s*(numerador+2)/(denominador+1)
    #s=s*num
    numerador=numerador+2
    denominador=denominador+2
    i=i+1
    
    
print(s)
pi=2*s
print('%.5f'%pi)