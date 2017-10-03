# -*- coding: utf-8 -*-
p1=float(input("Insira P1: "))
c1=float(input("Insira C1: "))
p2=float(input("Insira P2: "))
c2=float(input("Insira C2: "))
if p1*c1 == p2*c2:
    print("0")
if p1*c1 > p2*c2:
    print("-1")
if p1*c1 < p2*c2:
    print("1")