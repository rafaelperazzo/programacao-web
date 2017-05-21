# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um número:'))
a=2
b=1
i=0
cont=0
while i<=n: 
    if i%2!=0:
        pi=a/b
        cont=cont*pi
        b=b+1
    if i%2==0:
        pi=a/b
        cont=cont*pi
        a=a+1
    i=i+1
print(cont)
        