# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor de n: '))
produto=1
num=2
dem=1
contador=1
while (contador>n):
    produto=produto*(num/dem)
    if ((num/dem)>1):
        dem=dem+2
    elif ((num/dem)<1):
        num=num+2
    contador=contador+1
pi=produto*2
print('%.5f' %pi)
    