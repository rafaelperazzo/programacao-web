# -*- coding: utf-8 -*-
n=int(input('digite um n,inteiro e positivo: '))
i=1
fat=1
    while n<0 :
        n=int(input('opcao invalida,digite um inteiro positivo; '))
while i<=n :
    fat= i*fat
    i=i+1
print("%d"%fat)

