# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos: '))
produto=1
i=2
for i in range(2,n+1,2):
    produto=produto*(i/(i-1))*(i/(i+1))
produto=produto*2
print('%.5f'%produto)