# -*- coding: utf-8 -*-
n=int(input("Digite um número: '))
q=0
r=0
while (n>1):
    q=n/2
    r=n%2
    if (q>1):
        q=q/2
        r=q%2
        print(r)

