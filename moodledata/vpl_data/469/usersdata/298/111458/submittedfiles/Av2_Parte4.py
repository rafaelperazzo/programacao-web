# -*- coding: utf-8 -*-
while True:
    m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>=2 and m<=1000:
        break
    if m<2:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>1000:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))