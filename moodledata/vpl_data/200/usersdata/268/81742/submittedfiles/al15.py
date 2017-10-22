# -*- coding: utf-8 -*-
a=1000
b=9999
cont=0
while(a<9999):
    doisultimos= a%10**2
    doisprimeiros= (a-(a%10**2))*10**2
    if( a**(1/2) == (doisprimeiros+doisultimos)):
        print(a)
    a=a+1
    