# -*- coding: utf-8 -*-
n=int(input('escreva c:'))
m=int(input('escreva d:'))
cont=0
p=42195
for i in range(1,n+1,1):
    posto=int(input('escreva metros:'))
    if posto<=cont:
        cont=cont+m
if cont>=p:
    print('s')
else:
    print('n')
