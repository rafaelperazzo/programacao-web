# -*- coding: utf-8 -*-
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1<n2<n3 or n1<n3<n2:
    print("%.d" %(n1))
if n2<n1<n3 or n2<n3<n1:
    print("%.d" %(n2))
if n3<n1<n2 or n3<n2<n1:
    print("%.d" %(n3))