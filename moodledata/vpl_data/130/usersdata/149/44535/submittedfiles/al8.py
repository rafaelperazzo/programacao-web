# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
produto=0
for i in range(1,n+1,1):
    produto=produto+n*(n-i)
print(produto)
