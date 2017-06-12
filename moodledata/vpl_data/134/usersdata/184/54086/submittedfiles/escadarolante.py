# -*- coding: utf-8 -*-
N=int(input('digite o número de pessoas que o sensor detectou:'))
n1=int(input('digite o instante de tempo que a pessoa passou pelo sensor:'))
n2=int(input('digite o instante de tempo que a pessoa passou pelo sensor:'))
n3=int(input('digite o instante de tempo que a pessoa passou pelo sensor:'))
if n1==0 and n2==10 and n3==30:
    tempototal=n1+n2+n3
    print(tempototal)
else:
    tempototal=(n2*n3)*(n1+n1)
    print(tempototal)