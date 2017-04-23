# -*- coding: utf-8 -*-
A1=float(input('Digite o valor numérico A1:'))
A2=float(input('Digite o valor numérico A2:'))
A3=float(input('Digite o valor numérico A3:'))
A4=float(input('Digite o valor numérico A4:'))
if A1>A2 and A1>A3 and A1>A4:
    print(A1)
if A2>A1 and A2>A3 and A2>A4:
    print(A2)
if A3>A1 and A3>A2 and A1>A4:
    print(A3)
if A4>A1 and A4>A3 and A4>A3:
    print(A4)    
if A1<A2 and A1<A3 and A1<A4:
    print(A1)
if A1<A2 and A1>A3 and A1<A4:
    print(A2)
if A1<A2 and A1>A3 and A1<A4:
    print(A3)
if A1<A2 and A1>A3 and A1<A4:
    print(A4)