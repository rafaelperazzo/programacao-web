# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
produto=1
for i in range(0,n,1):
    produto=produto*(n-i)
    
print(produto)