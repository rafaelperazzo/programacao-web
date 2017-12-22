# -*- coding: utf-8 -*-
n = int(input(''))
total = 0
estoque = []
for i in range(n):
  tamanho = int(input(''))
  if tamanho in estoque:
    estoque.remove(tamanho)
    continue
  else:
    total = total+2
    estoque.append(tamanho)
print(total)
