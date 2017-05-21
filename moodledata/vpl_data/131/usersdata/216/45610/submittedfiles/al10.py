# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um número:'))
a=2
b=1
i=1
cont=1
while i<n: 
    cont=cont*(a/b)
    if i%2==1:
        a=a+1
    else:
        b=b+1
    i=i+1
print(cont)
        