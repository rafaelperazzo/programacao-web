# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos: '))
produto=1
i=2
for i in range(2,n+1,1):
    produto=produto*i*(i/(i+1))*((i+1)/(i+2))
    print('%.5f'%produto)