# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Número de termos: '))
num = 2
den = 1
i=1
MeioPi=1
while i<=n:
    MeioPi = MeioPi*(num/den)
    if i%2!=0:
        den=den+2
    else:
        num=num+2
    i=i+1
Pi=MeioPi*2
print('&.5f' %Pi)