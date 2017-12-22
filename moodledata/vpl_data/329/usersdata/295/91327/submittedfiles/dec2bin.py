# -*- coding: utf-8 -*-
p = int(input("Digite o primeiro numero :"))
while p<=0:
    p = int(input("Digite o primeiro numero :"))
q = int(input("Digite o segundo numero :"))
while q<=0:
    q = int(input("Digite o segundo numero :"))
if str(p) in str(q):
    print("S")
else:
    print("N")
    
