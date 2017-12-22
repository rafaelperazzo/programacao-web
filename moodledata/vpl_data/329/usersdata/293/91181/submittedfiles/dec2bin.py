# -*- coding: utf-8 -*-
q=int(input("Digite q: "))
n=0
while(True):
    if q//(10**n)>0:
        n=n+1
        print(n)
print(n+1)