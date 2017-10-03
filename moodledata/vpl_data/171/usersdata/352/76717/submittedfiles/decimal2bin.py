# -*- coding: utf-8 -*-


n=int(input('Digite o numero em binario:'))

S=0
i=0

while n>0:
    ultimo=n%10
    S=S+(ultimo*(2**i))
    i=i+1
    n=n//10
print(S)