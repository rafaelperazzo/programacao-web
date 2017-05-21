# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um número:'))
a=2
b=1
i=0
cont=1
while i<=(n-1): 
    cont=cont*(a/b)
    if i%2==1:
        a=a+2
    else:
        b=b+2
    i=i+1
    
cont=cont*2
print('%.2f'%cont)
        