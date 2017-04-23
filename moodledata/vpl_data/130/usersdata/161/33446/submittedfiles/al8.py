# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
i=1
for i in range(2,n+1):
    n=n*i
    print('%d!=d%' (n,i))