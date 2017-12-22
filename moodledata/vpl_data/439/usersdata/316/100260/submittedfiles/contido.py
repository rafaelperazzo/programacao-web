# -*- coding: utf-8 -*-
nm=int(input('digite o numero de elementos da primeira lista: '))
mn=int(input('digite o numero de elementos da segunda lista: '))
da=[]
vi=[]

for i in range (0,nm,1):
    valor_da=float(input('digite um elemento da primeira lista: '))
    da.append (valor_da)
for i in range (0,mn,1):
    valor_vi=float(input('digite um elemento da segunda lista: '))
    vi.append (valor_vi)
    
def intersecao(da, vi):
    return list(set(da) & set(vi))
intersecao=intersecao(da,vi)
print(len(intersecao))
