# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite um valor: '))
if  n<0:
    n=n*(-1)
    s=0
    i=1
    d=n
    while i<=n:
        s=s+i/d
        i=i+1
        d=d-1
    print('%.5f'%s)
else:
    s=0
    i=1
    d=n
    while i<=n:
        s=s+i/d
        i=i+1
        d=d-1
    print('%.5f'%s)
        
