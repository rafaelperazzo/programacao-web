# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite n:'))
produto=1
for i in range (1,n+1,1):
    if i%2!=0:
        produto=(i+1)/i
    else:
        produto=i/(i+1)
pi=produto*2
print('O valor aproximado de pi é: %.5f' %pi)