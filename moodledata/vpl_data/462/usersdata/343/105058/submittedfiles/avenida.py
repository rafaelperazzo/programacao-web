# -*- coding: utf-8 -*-
M = int(input("número de quadras no sentido norte-sul: "))
N = int(input("número de quadras no sentito leste-oeste: "))
bairro = []
for i in range(N) :
    elementos = []
    for j in range(M) :
        elementos.append(int(input("valor de cada quadra: ")))
    bairro.append(elementos)
print(bairro)