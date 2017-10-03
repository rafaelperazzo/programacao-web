# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos : '))
produto= 1
num=2
den=1
cont=1
while(cont<=n):
    produto=produto * (num/den)
    if (num/den)>1:
        den=den+2
    elif (num/den)<1:
        num=num+2
    cont=cont + 1
pi= (produto)*2
print('%.5f' %pi)
    