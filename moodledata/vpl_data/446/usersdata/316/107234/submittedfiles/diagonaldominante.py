# -*- coding: utf-8 -*-
m=int(input('digite a ordem da matriz: '))
lista=[]
for i in range(0,m,1):
    c=[]
    for j in range(0,m,1):
        c.append(float(input('digite o valor da linha %d e da coluna %d: ' %((j+1),(i+1)))))
    lista.append(c)
print(lista)

if lista[0][0]>(lista[0][1]+lista[0][2]):
    if lista[1][1]>(lista[1][0]+lista[1][2]):
        if lista[2][2]>(lista[2][0]+lista[2][1]):
            print('SIM')
        else:
            print('NÃO')
    else:
        print('NÃO')
else:
    print('NÃO')
