# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um número:'))
a=2
b=1
i=0
cont=0
while i<n: 
    pi=a/b
    if i%2!=0:
        cont=cont*pi
        b=b+1
    else i%2==0:
        cont=cont*pi
        a=a+1
    i=i+1
print(cont)
        