# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
produto=1
num=2
den=1
for i in range(1,n+1,1):
    produto=produto*(num/den)
    if i%2==1:
        den=den+2
    else:
        num=num+2
produto=produto*2
print('%.5f'%produto)
