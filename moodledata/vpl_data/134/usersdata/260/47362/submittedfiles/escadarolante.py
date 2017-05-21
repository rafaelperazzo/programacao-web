# -*- coding: utf-8 -*-
N=int(input("determine o número de pessoas na escada rolante:"))
s=0
m=int(input("determine o instante em que o primeiro cliente sobe a escada:"))
for i in range (1,N,1):
    n=int(input("determine o instante em que o cliente posterior sobe a escada:"))
    if m+10-n >=0:
        s=n-m+s
    else:
        s=s+10
    m=n
    print(s)
s=s+10
print(s)