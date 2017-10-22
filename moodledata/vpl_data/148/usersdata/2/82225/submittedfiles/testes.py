# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de termos:'))
s=1
i=1
while i<=n:
       s=s*((2*i)/(2*i-1))*((2*i)/(2*i+1))
       i=i+1
pi=2*s
print('%.5f' %pi)