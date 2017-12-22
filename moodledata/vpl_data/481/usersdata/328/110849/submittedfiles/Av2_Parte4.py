# -*- coding: utf-8 -*-
o=int(input('Ordem da matriz:'))
ma=[]
for i in range(o):
    lista=[]
    for j in range(o):
        lista.append(int(input('Elementos da matriz:')))
    ma.append(lista)
if ma[0]+ma[i]>ma[0]+ma[j]:
    print('A')
else:
    print("foda")



print(ma)
print(len(ma))
