# -*- coding: utf-8
n=int(input("Digite o numero na baze binaria:"))
zoma=0
i=0
while(n/10)>0:
    A=n%10
    zoma=zoma+(A*(2**i))
    n=n//10
    i=i+1
print(zoma)

