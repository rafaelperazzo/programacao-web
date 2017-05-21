# -*- coding: utf-8 -*-
N=int(input("determine o número de pessoas na escada rolante:"))
r=float(input("determine o instante em que o primeiro cliente sobe a escada:"))
s=0
for i in range (1,N,1):
    m=int(input("determine o instante em que o cliente anterior sobe a escada:"))
    n=int(input("determine o instante em que o cliente posterior sobe a escada:"))
    if r+10- m>=0:
        s=s+10
    else:
        s=m-r+s
    r=m
print(s)