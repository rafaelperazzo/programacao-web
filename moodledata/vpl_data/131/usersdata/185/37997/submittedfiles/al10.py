# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor de n:'))
produto=2
num=2
den=1
for i in range (1,n+1,1):
    if i%2==0:
        produto=produto*(num/den+2)
        den=den+2
    else:
        produto=produto*(num+2/den)
    num=num+2
print('%.5f' %produto)
