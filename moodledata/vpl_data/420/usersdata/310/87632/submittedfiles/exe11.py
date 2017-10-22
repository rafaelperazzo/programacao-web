# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n: ' ))
soma =0
t = 10000000
if n > 9999999 and n < 100000000:
    for i in range (0,9,1):
       i=n//t
       soma = soma+n
       n=n%t
       t=t/10
    print (soma)

else:
    print('NAO SEI')












