# -*- coding: utf-8 -*-
a=int(input('digite o número:'))
b=int(input('digite o número:'))
conta=0
contb=0
for i in range(1,a+1,1):
    if a%i==0:
        conta=conta+1
        if conta>=3:
            print('N')
for i in range(1,b+1,1):
    if b%i==0:
        conta=conta+1
        if contb>=3:
            print('N')
            









if b==a+2:
    print('S')
else:
    print('N')