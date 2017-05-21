# -*- coding: utf-8 -*-
N=int(input("determine o número de pessoas na escada rolante:"))
for i in range (,(n+1)/2,1):
    m=int(input("determine o instante em que o cliente sobe a escada:"))
    n=int(input("determine o instante em que o cliente posterior sobe a escada:"))
    if m+10-n=>0:
        s=s+10
    else:
        s=n-m+s