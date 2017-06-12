# -*- coding: utf-8 -*-
x=int(input('digite x:'))
m=int(input('digite m:'))
cont=0
p=42195
for i in range (1,x+1,1):
    posto=int(input('digite metros:'))
    if posto<=cont:
        cont=cont+m
if cont>=p:
    print('s')
else:
    print('n')