# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos:'))


s=0
i=1

while i<n:
    s=s*((2*i)/(2*i-1))*((2*i)/(2*i+1))
    i=i+1
    

    
print(s)
pi=2*s
print('%.5f'%pi)