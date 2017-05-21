# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n= int(input('Digite o numero de termos:'))
 m=1
for i in range (2,n+1,1):
    if (i%n==0):
        m=m(i/n)*(i/n+1)
    else: 
        m=m((i+2)/n-1)*(i/n+1)
print (m)