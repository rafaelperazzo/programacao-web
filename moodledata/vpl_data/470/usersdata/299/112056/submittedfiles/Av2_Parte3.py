# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de listas: '))
m=int(input('Digite a quantidade de elementos que as listas vão ter: '))
main=[]
for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(int(input('Digite o elemento %d da lista %k' %(j+1,i+1))))
    main.append(linha)
print(main)
