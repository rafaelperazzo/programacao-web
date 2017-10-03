# -*- coding: utf-8 -*-
p1=float(input("\nDigite o peso da criança do lado esquerdo: "))
c1=float(input("\nDigite o comprimento esquerdo: "))
p2=float(input("\nDigite o peso da criança do lado direito: "))
c2=float(input("\nDigite o comprimento direito: "))

if p1*c1==p2*c2:
    print("0")
elif p1*c1>p2*c2:
    print("-1")
elif p1*c1<p2*c2:
    print("1")


