# -*- coding: utf-8 -*-
a=int(input("Digite o dia X: "))
b=int(input("Digite o mês X: "))
c=int(input("Digite o ano X: "))
e=int(input("Digite o dia Y: "))
f=int(input("Digite o mês Y: "))
g=int(input("Digite o ano Y: "))

if c>g:
    print("DATA1")
if g>c:
    print("DATA2")
if g=c:
    if b>f:
        print("DATA1")
    elif f>b:
        print("DATA2")
    elif b=f:
        if b>f:
            print("DATA1")
        elif f>b:
            print("DATA2")
else:
    print("IGUAIS")
