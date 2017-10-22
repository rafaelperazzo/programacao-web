# -*- coding: utf-8 -*-
n=int(input('digite um n,inteiro e positivo: '))
i=1
fat=1
if n>=0 :
    while i<=n :
        fat= i*fat
        i=i+1
    print("%d"%fat)
else :
    n=int(input('opcao invalida,digite um inteiro positivo; '))
