# -*- coding: utf-8 -*-
for i in range(1000,9999,1):
    raiz=(i**1/2)
    DI=i//100
    RE=i%100
    numero=DI+RE
    if raiz==numero:
        print(numero)
        