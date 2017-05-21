# -*- coding: utf-8 -*-
N=int(input("determine o número de pessoas na escada rolante:"))
s=0
for i in range (1,N,1):
    m=int(input("determine o instante em que o cliente anterior sobe a escada:"))
    n=int(input("determine o instante em que o cliente posterior sobe a escada:"))
    if m+10-n>=0:
        s=s+10
         m=n
         n=n+10
        if m+10-n>=0:
            s=s+10
        else:
            s=n-m+s
    else:
        s=n-m+s
    m=n
    n=n+10
    if m+10-n>=0:
        s=s+10
    else:
        s=n-m+s
print(s)