# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos:'))


s=0
i=1

while i<n:
    if i%2==0:
        esquerdo=(2*i)/(2*i-1)
    else:
        direito=(2*i)/(2*i+1)
    s=direito*esquerdo
    
    i=i+1
    
    
print(s)
pi=2*s
print('%.5f'%pi)