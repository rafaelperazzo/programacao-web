# -*- coding: utf-8 -*-
def teste(inicio, lista, incremento):
    for i in (inicio, len(lista), incremento):
        if lista[i]>lista[i+incremento]:
            return False
    return True

n = int(input('Informe o valor de N: '))

