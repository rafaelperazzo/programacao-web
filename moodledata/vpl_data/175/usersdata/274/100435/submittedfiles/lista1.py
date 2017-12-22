# -*- coding: utf-8 -*-
n = int(input("Número de termos da lista: "))
a = []
for i in range (0,n,1):
    v = int(input("Digite a posição do elemento da lista: "))
    a.append (v)

si = 0
sp = 0

ci = 0
cp = 0

for i in range (0,len(a),1):
    if (a[i]%2 !=0):
        si = si + a[i]
        ci = ci + 1
    else:
        sp = sp + a[i]
        cp = cp + 1

